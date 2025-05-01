from otp.otpbase.OTPModules import StringStream
from direct.distributed.PyDatagram import PyDatagram
import random
from otp.otpbase.OTPModules import ConfigVariableInt, ConfigVariableDouble

class ClsendTracker:
    
    clsendNotify = directNotify.newCategory("clsend")
    
    # How many trackers can log overflow
    NumTrackersLoggingOverflow = 0
    MaxTrackersLoggingOverflow = ConfigVariableInt('max-clsend-loggers', 5).getValue()

    def __init__(self):
        # Overflow logging is disabled by default
        self._logClsendOverflow = False
        
        # Make sure they're a player
        if self.isPlayerControlled():
            # Check if AIRepository has it enabled
            if simbase.air.getTrackClsends():
                # Check if the loggers are below the limit
                if ClsendTracker.NumTrackersLoggingOverflow < ClsendTracker.MaxTrackersLoggingOverflow:
                    # Now log 1 out of N avatars (4 in dev, and 50 in live/test)
                    self._logClsendOverflow = (
                        random.random() < 1.0 / 
                        ConfigVariableDouble('clsend-log-one-av-in-every', choice(__dev__, 4, 50)).getValue())
        
        if self._logClsendOverflow:
            # Increase the counter by 1 for each logger
            ClsendTracker.NumTrackersLoggingOverflow += 1
        
        # Default values for message collection
        self._clsendMsgs = []
        self._clsendBufLimit = 100
        self._clsendFlushNum = 20
        self._clsendCounter = 0

    def announceGenerate(self):
        # Start logging overflows
        if self._logClsendOverflow:
            self.clsendNotify.info("logging all clsends for %s" % self.doId)

    def destroy(self):
        if self._logClsendOverflow:
            # Decrease the counter by 1 for each logger
            ClsendTracker.NumTrackersLoggingOverflow -= 1

    def trackClientSendMsg(self, dataStr):
        # Add sent messages to the buffer
        self._clsendMsgs.append((self.air.getAvatarIdFromSender(), dataStr))
        # If there's more than the specified limit (default 100) remove the oldest
        if len(self._clsendMsgs) >= self._clsendBufLimit:
            self._trimClsend()

    def _trimClsend(self):
        # How many messages to flush at once (default 20)
        for i in range(self._clsendFlushNum):
            # If logging is enabled log the oldest message
            if self._logClsendOverflow:
                self._logClsend(*self._clsendMsgs[0])
            # Otherwise remove the oldest message
            self._clsendMsgs = self._clsendMsgs[1:]
            # And increase the counter by 1
            self._clsendCounter += 1

    def _logClsend(self, senderId, dataStr):
        # Turn the message into a readable format
        msgStream = StringStream()
        simbase.air.describeMessage(msgStream, '', dataStr)
        readableStr = msgStream.getData()
        
        # Get a hex dump of the message
        sstream = StringStream()
        PyDatagram(dataStr).dumpHex(sstream)
        hexDump = sstream.getData()
        
        # Print out the message
        self.clsendNotify.info("%s [%s]: %s%s" % (
            self.doId, self._clsendCounter, readableStr, hexDump))

    def dumpClientSentMsgs(self):
        # Go through all messages
        for msg in self._clsendMsgs:
            # Now log them
            self._logClsend(*msg)
            # And increase the counter by 1
            self._clsendCounter += 1
