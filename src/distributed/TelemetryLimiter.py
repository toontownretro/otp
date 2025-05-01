from direct.showbase.DirectObject import DirectObject
from otp.avatar.DistributedPlayer import DistributedPlayer
from direct.task.Task import Task

class TelemetryLimiter(DirectObject):
    
    TaskName = "TelemetryLimiterEnforce"
    LeakDetectEventName = "telemetryLimiter"

    def __init__(self):
        # Create a dict for objects
        self._objs = {}
        #  Setup a task to enforce all limits
        self._task = taskMgr.add(self._enforceLimits, self.TaskName, priority = 40)

    def destroy(self):
        # clean up the task and remove all objects
        taskMgr.remove(self._task)
        del self._objs

    def getNumObjs(self):
        # Returns how many objects are currently being tracked
        return len(self._objs)

    def addObj(self, obj):
        # Add an object for tracking
        id = obj.getTelemetryLimiterId()
        self._objs[id] = obj
        # Listen for events
        self.accept(self._getDummyEventName(obj), self._dummyEventHandler)

    def _getDummyEventName(self, obj):
        # Creates an event name for an object and
        # keeps track of its ID and class
        return "%s-%s-%s-%s" % (self.LeakDetectEventName,
            obj.getTelemetryLimiterId(), id(obj), obj.__class__.__name__)

    def _dummyEventHandler(self, *args, **kargs):
        # dummy class to keep things nice and quiet
        pass

    def removeObj(self, obj):
        # Stop tracking an object
        id = obj.getTelemetryLimiterId()
        self._objs.pop(id)
        # Stop listening for events
        self.ignore(self._getDummyEventName(obj))

    def _enforceLimits(self, task = None):
        # enforces limits on all tracked objects
        for obj in list(self._objs.values()):
            obj.enforceTelemetryLimits()
        # Repeat it for every frame
        return Task.cont

# Parent class this should be used as
# a base when adding additional limiters
# i.e RotationLimitToH
class TelemetryLimit:

    def __call__(self, obj):
        # Do nothing
        pass

# Forcefully sets the pitch and roll constant of a player to 0
# This should be called in relation with TLGatherAllAvs
class RotationLimitToH(TelemetryLimit):

    def __init__(self, pConst = 0.0, rConst = 0.0):
        # set pitch and roll to 0
        self._pConst = pConst
        self._rConst = rConst

    def __call__(self, obj):
        # Custom: To fix crashing
        if obj.isEmpty():
            return
        # Apply forced constant for pitch and roll
        # while leaving heading unchanged
        obj.setHpr(obj.getH(), self._pConst, self._rConst)

# This should only be called in connection with config.getBool
# to either choose between allowing (TLGatherAllAvs) or
# disallowing (TLNull) telemetry
class TLNull:

    def __init__(self, *limits):
        # Do nothing
        pass

    def destroy(self):
        # Do nothing
        pass

# Gathers all avatars in a zone/instance
# and add a telemetry limiter to them
class TLGatherAllAvs(DirectObject):

    def __init__(self, name, *limits):
        self._name = name
        self._avs = {}
        self._limits = makeList(limits)
        self._avId2limits = {}
        avs = base.cr.doFindAllInstances(DistributedPlayer)
        # Start the player limiter
        for av in avs:
            self._handlePlayerArrive(av)

        # Listen for events when a player arrives and leaves
        self.accept(DistributedPlayer.GetPlayerGenerateEvent(), self._handlePlayerArrive)
        self.accept(DistributedPlayer.GetPlayerNetworkDeleteEvent(), self._handlePlayerLeave)

    def _handlePlayerArrive(self, av):
        """Adds the player to the telemetry limitations"""
        # Skip if they're a localAvatar
        if av is not localAvatar:
            self._avs[av.doId] = av
            limitList = []
            # Add the player
            for limit in self._limits:
                l = limit()
                limitList.append(l)
                av.addTelemetryLimit(l)
            # Add all limits
            self._avId2limits[av.doId] = limitList
            base.cr.telemetryLimiter.addObj(av)

    def _handlePlayerLeave(self, av):
        """Removes the player from any telemetry limitations"""
        # Skip if they're a localAvatar
        if av is not localAvatar:
            base.cr.telemetryLimiter.removeObj(av)
            # Remove all limits
            for limit in self._avId2limits[av.doId]:
                av.removeTelemetryLimit(limit)
            # clean up the removal 
            del self._avId2limits[av.doId]
            del self._avs[av.doId]

    def destroy(self):
        """Disable all TLGatherAllAvs telemetry"""
        self.ignoreAll()
        # Lift all restrictions
        while len(self._avs):
            self._handlePlayerLeave(list(self._avs.values())[0])
        # clean up the removal
        del self._avs
        del self._limits
        del self._avId2limits
