"""
all info about ChannelManager.py I could find:

otp/switchboard/sbNode.py

class sbNode(Pyro.core.SynchronizedObjBase,ChannelListener):
    def __init__(self,
                 nodeName,
                 wedgeName="",
                 nsHost=None,
                 nsPort=None,
                 listenPort=None,
                 clHost=None,
                 clPort=None,
                 chanMgr=None,
                 dislURL=None):
        
        ChannelListener.__init__(self,nodeName,chanMgr)

        Pyro.config.PYRO_MULTITHREADED = 0

        Pyro.core.SynchronizedObjBase.__init__(self)
        Pyro.core.initServer(banner=0)

        self.log = sbLog(":sb.node.%s"%nodeName,clHost,clPort)

        self.nodeName = nodeName
        if wedgeName == "":
            self.wedgeName = nodeName
        else:
            self.wedgeName = wedgeName

        self.wedge = None
        self.nodeList = []
        self.nodeProxy = {}

        self.id2Friends = {}

        self.log.info("Starting.")

        # DISL SOAP init (temporary)
        from .PlayerFriendsDB import PlayerFriendsDB
        self.friendsDB = PlayerFriendsDB(self.log,dislURL)

        # DISL MD init
        self.channelList = [sbConfig.DISL2SBChannel,sbConfig.DISL2SBChannel+self.nodeName]
        self.joinChannels()
        
        # db init

        from .LastSeenDB import LastSeenDB
        self.lastSeenDB = LastSeenDB(log=self.log,
                                     host=sbConfig.lastSeenDBhost,
                                     port=sbConfig.lastSeenDBport,
                                     user=sbConfig.lastSeenDBuser,
                                     passwd=sbConfig.lastSeenDBpasswd,
                                     dbname=sbConfig.lastSeenDBdb)

        from .sbMaildb import sbMaildb
        self.mailDB = sbMaildb(log=self.log,
                               host=sbConfig.mailDBhost,
                               port=sbConfig.mailDBport,
                               user=sbConfig.mailDBuser,
                               passwd=sbConfig.mailDBpasswd,
                               db=sbConfig.mailDBdb)
                               
        # pyro init
        
        self.initPyro(nsHost,nsPort,listenPort)

        self.updateWedge()
        self.updateNodes()

        self.log.debug("Enter sendEnterNode")
        self.sendEnterNode()
        self.log.debug("Exit sendEnterNode")

        self.localPlayers = {}
        self.remotePlayerLoc = {}
        self.remotePlayerInfo = {}

        self.servedLogins = 0        
        self.servedChat = 0
        self.servedChatSC = 0
        self.servedMail = 0
        self.servedMailSC = 0

        self.log.info("-- sb.node.%s is ready. --" %self.nodeName)


    #wedge->node
    def recvEnterLocalPlayer(self,playerId,playerInfo):
        if playerId in self.localPlayers:
            self.log.warning("Warning: enterPlayer(%d) called, but I already have this player."%(playerId))

        self.log.debug("Player %d entered." % (playerId))
        self.servedLogins = self.servedLogins + 1

        #self.log.debug("PlayerInfo.onlineYesNo = %d" % playerInfo.onlineYesNo)

        self.localPlayers[playerId] = playerInfo
        self.id2Friends[playerId] = {}

        # get friends list asynchronously, DISL will send it back
        # and hit handleDISLSendFriendAdd
        try:
            self.log.debug("Sending msg to DISL: %s %s %s %s" % (sbConfig.SB2DISLChannel,
                                                                 sbConfig.DISL2SBChannel+self.nodeName,
                                                                 sbConfig.FC_DISLGetFriends,
                                                                 "%d"%playerId))
            self.broadcastMessage(ChannelMessage(sbConfig.SB2DISLChannel,
                                                 sbConfig.DISL2SBChannel+self.nodeName,
                                                 sbConfig.FC_DISLGetFriends,
                                                 "%d"%playerId))
        except Exception as e:
            self.log.error("Error sending friends request to DISL:")
            self.log.error(''.join(Pyro.util.getPyroTraceback(e)))

        if playerInfo:
            self.lastSeenDB.setInfo(playerId,playerInfo)


otp/switchboard/startNode.py

from otp.switchboard.xd.ChannelManager import *

cm = ChannelManager()
ncm = NetChannelMessenger(nodename,cm,dshost,dsport,1,1000000)

myNode = sbNode(nodeName=nodename,nsHost=nshost,nsPort=nsport,listenPort=nodeport,clHost=clhost,clPort=clport,chanMgr=cm,dislURL=dislurl)

sys.stdout.flush()

try:
    while 1:
        myNode.pyroDaemon.handleRequests(0)
        ncm.pump()
        if ncm.checkReconnect():
            cm.addPromiscuousListener(ncm)
            myNode.joinChannels()
        time.sleep(0.01)
finally:
    #try:
    #    myNode.pyroDaemon.shutdown(True)
    #except: pass
    sys.stdout.flush()

"""

# Does it import anything at all???
# Possible imports below:
# from otp.switchboard.sbNode import *
# from otp.switchboard.startNode import *
# import Pyro.core
# import Pyro.naming
# import Pyro.errors
# import Pyro.util
# import Pyro.warning

class ChannelManager:
    def __init(self):
        pass

class ChannelMessage:
    def __init__(self):
        pass

    def addPromiscuousListener(self, NetChannelMessenger):
        pass
    
    # ?
    def removePromiscuousListener(self, NetChannelMessenger):
        pass
    
    # sbNode.py
    def broadcastMessage(self, ChannelMessage):
        pass

class NetChannelMessenger:
    def __init__(self,nodeName,channelManager,dsHost,dsPort,arg1,arg2):
        self.nodeName = nodeName
        self.channelManager = channelManager
        self.dsHost = dsHost
        self.dsPort = dsPort

    def pump(self):
        pass

    def checkReconnect(self):
        pass

class ChannelListener:
    def __init__(self,nodeName,chanMgr):
        self.nodeName = nodeName
        self.chanMgr = chanMgr
    
    # sbNode.py
    def broadcastMessage(self, channelMessage):
        pass
