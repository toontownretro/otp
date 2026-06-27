import os, time, random, datetime, subprocess

import mariadb

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.fsm.FSM import FSM
from direct.fsm.StatePush import StateVar, FunctionCall
from direct.showbase.DirectObject import DirectObject
from direct.task import Task
from direct.showbase.Job import Job
from direct.stdpy import threading # MySQLdb blocks on locked table access
from otp.sql.DBInterface import DBInterface
from otp.sql.SqlErrors import *

from otp.otpbase.OTPModules import *

class TryAgainLater(Exception):
    def __init__(self, sqlException, address):
        self._exception = sqlException
        self._address = address

    def getSQLException(self):
        return self._exception

    def __str__(self):
        return 'Problem using SQL DB at %s, try again later (%s)' % (self._address, self._exception)
        
class SqlDBCursorBase:
    notify = directNotify.newCategory('SqlDBConnection')
    
    ConnectionProblems = set([ServerShuttingDown, ServerGoneAway])
    
    def __init__(self):
        self._manager = None
    
    def setManager(self, manager):
        self._manager = manager

    def _doExecute(self, cursorBase, *args, **kArgs):
        if self.notify.getDebug():
            self.notify.debug('execute:\n%s' % (args[0]))
        try:
            cursorBase.execute(self, *args, **kArgs)
        except OperationalError as e:
            if e.errno in SqlDBCursorBase.ConnectionProblems:
                # force a reconnect
                self._manager._db = None
                raise TryAgainLater(e, '%s:%s' % (self._manager._host, self._manager._port))
            else:
                raise
                
class SqlDBCursor(mariadb.cursors.Cursor, SqlDBCursorBase):
    notify = directNotify.newCategory('SqlDBConnection')
    
    def __init__(self, connection, **kwargs):
        mariadb.cursors.Cursor.__init__(self, connection, **kwargs)
        SqlDBCursorBase.__init__(self)

    def execute(self, *args, **kArgs):
        self._doExecute(mariadb.cursors.Cursor, *args, **kArgs)
        
class SqlDBBinaryCursor(mariadb.cursors.Cursor, SqlDBCursorBase):
    notify = directNotify.newCategory('SqlDBConnection')
    
    def __init__(self, connection, **kwargs):
        kwargs["binary"] = True
        mariadb.cursors.Cursor.__init__(self, connection, **kwargs)
        SqlDBCursorBase.__init__(self)

    def execute(self, *args, **kArgs):
        self._doExecute(mariadb.cursors.Cursor, *args, **kArgs)
        
class SqlDBDictCursor(mariadb.cursors.Cursor, SqlDBCursorBase):
    notify = directNotify.newCategory('SqlDBConnection')
    
    def __init__(self, connection, **kwargs):
        kwargs["dictionary"] = True
        mariadb.cursors.Cursor.__init__(self, connection, **kwargs)
        SqlDBCursorBase.__init__(self)

    def execute(self, *args, **kArgs):
        self._doExecute(mariadb.cursors.Cursor, *args, **kArgs)
        
class SqlDBConnection(DBInterface):
    notify = directNotify.newCategory('SqlDBConnection')

    RetryPeriod = 5.
    TableLockRetryPeriod = 1.

    Connecting = 'Connecting'
    Initializing = 'Initializing'
    Locking = 'Locking'
    Connected = 'Connected'
    Disconnected = 'Disconnected'
    Released = 'Released'
    WaitForRetry = 'WaitForRetry'
    WaitForRetryLocking = 'WaitForRetryLocking'

    READ = 'READ'
    WRITE = 'WRITE'

    LoggedConnectionInfo = False
    ConnectedEvent = 'SqlDBConnection-Connected-%s'

    WantTableLocking = ConfigVariableBool('want-sql-db-locking', 0).getValue()
    
    ConnectFunction = mariadb.connect
    ConnectRetryTimeout = 3.

    def __init__(self, connectInfo, tableLocks={}):
        # tableLocks: table name -> READ||WRITE
        self._host = connectInfo.host
        self._port = connectInfo.port
        self._user = connectInfo.user
        self._passwd = connectInfo.passwd
        self._tableLocks = tableLocks
        self._db = None
        self._dbName = connectInfo.dbname
        self._lastFailedConnectTime = None
        self._retryDoLater = None
        self._retryLockingDoLater = None
        self._curState = 'Off'
        self.request(self.Connecting)

    # hack FSM to allow request in enter methods
    def request(self, state):
        exitFuncName = 'exit%s' % self._curState
        if hasattr(self, exitFuncName):
            getattr(self, exitFuncName)()
        enterFuncName = 'enter%s' % state
        self._curState = state
        if hasattr(self, enterFuncName):
            getattr(self, enterFuncName)()
            
    def getState(self):
        return self._curState

    def destroy(self):
        self.release()
        self.request('Off')
        self._db = None

    def getConnectedEvent(self):
        return self.ConnectedEvent % id(self)

    def isConnected(self):
        return self._curState == self.Connected

    def isDisconnected(self):
        return self._curState == self.Disconnected
        
    def isOff(self):
        return self._curState == 'Off'
        
    def isDisabled(self):
        return self.isOff() or self.isDisconnected()

    def getDb(self):
        # Returns valid sql db when in Connected state
        return self._db

    def getCursor(self, **kwargs):
        if not self._db:
            return None
        cursor = self._db.cursor(SqlDBCursor, **kwargs)
        cursor.setManager(self)
        return cursor
        
    def getBinaryCursor(self, **kwargs):
        if not self._db:
            return None
        cursor = self._db.cursor(SqlDBBinaryCursor, **kwargs)
        cursor.setManager(self)
        return cursor

    def getDictCursor(self, **kwargs):
        if not self._db:
            return None
        cursor = self._db.cursor(SqlDBDictCursor, **kwargs)
        cursor.setManager(self)
        return cursor
        
    def commit(self):
        self._db.commit()
        
    def connect(self):
        self.request(self.Connecting)

    def release(self):
        self.request('Released')
        
    def reconnect(self):
        self.request(self.WaitForRetry)
        
    def enterConnecting(self):
        if self._lastFailedConnectTime is not None:
            if (globalClock.getRealTime() - self._lastFailedConnectTime) < self.ConnectRetryTimeout:
                raise TryAgainLater(None, '%s:%s' % (self._host, self._port))

        if self._db:
            # no DB initialization required since we're already connected
            self.request(self.Locking)
            return

        try:
            self._db = self.__class__.ConnectFunction(host=self._host, port=self._port, user=self._user, password=self._passwd)
        except OperationalError as e:
            """
            self.notify.warning("Failed to connect to SQL database at %s:%d. Retrying in %s seconds."%(
                self._host,self._port,self.RetryPeriod))
            self.request(self.WaitForRetry)
            """
            self.notify.warning(str(e))
            self._lastFailedConnectTime = globalClock.getRealTime()
            raise TryAgainLater(e, '%s:%s' % (self._host, self._port))
        else:
            #self._db.set_character_set('utf8')

            # spammy
            if not self.__class__.LoggedConnectionInfo:
                self.notify.debug("Connected to SQL database at %s:%d." % (self._host,self._port))
                self.__class__.LoggedConnectionInfo = True
            self.request(self.Initializing)
            
    def _createTable(self, command):
        cursor = self.getCursor()
        try:
            cursor.execute(command)
        except OperationalError as e:
            if e.errno != TableAlreadyExists:
                raise
        except mariadb.Error as e:
            raise
                
    def enterInitializing(self):
        self.notify.error("enterInitializing - UNIMPLEMENTED. Please implement in a derived class.")
        
    def enterLocking(self):
        try:
            if not self.WantTableLocking:
                return

            if len(self._tableLocks):
                cmd = 'LOCK TABLES '
                for table, lock in list(self._tableLocks.items()):
                    cmd += '%s %s, ' % (table, lock)
                cmd = cmd[:-2] + ';'
                self.getCursor().execute(cmd)
        except TryAgainLater as e:
            self.notify.warning('Failed to acquire table lock(s), Retrying in %s seconds' % (self.TableLockRetryPeriod))
            self.request(self.WaitForRetryLocking)
        else:
            # spammy
            #self.notify.info("tables locked")
            self.request(self.Connected)
            
    def enterConnected(self):
        messenger.send(self.getConnectedEvent())

    def enterDisconnected(self):
        pass

    def exitDisconnected(self):
        pass
        
    def enterWaitForRetry(self):
        if self._retryDoLater:
            taskMgr.remove(self._retryDoLater)
        self._retryDoLater = taskMgr.doMethodLater(self.RetryPeriod, self._retryConnect, 'SqlDBConnection-retryConnect-%s' % id(self))

    def _retryConnect(self, task=None):
        self.request(self.Connecting)
        return Task.done

    def exitWaitForRetry(self):
        if not self._retryDoLater: return
        taskMgr.remove(self._retryDoLater)
        self._retryDoLater = None
            
    def enterWaitForRetryLocking(self):
        if self._retryLockingDoLater:
            taskMgr.remove(self._retryLockingDoLater)
        self._retryLockingDoLater = taskMgr.doMethodLater(self.RetryLockingPeriod, self._retryLocking, 'SqlDBConnection-retryLocking-%s' % id(self))

    def _retryLockingDoLater(self, task=None):
        self.request(self.Locking)
        return Task.done

    def exitWaitForRetryLocking(self):
        if not self._retryLockingDoLater: return
        taskMgr.remove(self._retryLockingDoLater)
        self._retryLockingDoLater = None
            
    def enterReleased(self):
        if not self.WantTableLocking: return
        if len(self._tableLocks):
            self.getCursor().execute('UNLOCK TABLES;')
            
class SqlDB(DBInterface, DirectObject):
    notify = directNotify.newCategory('SqlDB')

    TryAgainLater = TryAgainLater

    READ = SqlDBConnection.READ
    WRITE = SqlDBConnection.WRITE

    def __init__(self, host, port, user, passwd, dbname):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbname = self.processDBName(dbname)