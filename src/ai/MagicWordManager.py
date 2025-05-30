from otp.otpbase.OTPModules import *
from direct.showbase import GarbageReport, ContainerReport, MessengerLeakDetector
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.InputStateGlobal import inputState
from direct.showbase.ObjectCount import ObjectCount
from direct.task import Task
from direct.task.TaskProfiler import TaskProfiler
from otp.avatar import Avatar
import string
from direct.showbase import PythonUtil
from direct.showbase.PythonUtil import Functor, DelayedCall, ScratchPad
from otp.otpbase import OTPGlobals
from direct.distributed.ClockDelta import *
from direct.showutil.TexViewer import TexViewer

class MagicWordManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory("MagicWordManager")
    neverDisable = 1

    GameAvatarClass = None

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.shownFontNode = None
        self.csShown = 0
        self.guiPopupShown = 0
        self.texViewer = None

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.accept("magicWord", self.b_setMagicWord)
        self.autoMagicWordEvent = localAvatar.getArrivedOnDistrictEvent()
        if localAvatar.isGeneratedOnDistrict():
            self.doLoginMagicWords()
        else:
            self.accept(self.autoMagicWordEvent, self.doLoginMagicWords)

    def doLoginMagicWords(self):
        # MPG - we probably want generic versions of these
        """
        if ConfigVariableBool('want-chat', 0).getValue():
            # Automatically send ~chat if want-chat is true.
            self.d_setMagicWord('~chat', base.localAvatar.doId, 0)
        if ConfigVariableBool('want-run', 0).getValue():
            self.toggleRun()
        if ConfigVariableBool('immortal-mode', 0).getValue():
            self.d_setMagicWord('~immortal', base.localAvatar.doId, 0)
        """
        pass

    def disable(self):
        self.ignore(self.autoMagicWordEvent)
        del self.autoMagicWordEvent
        self.ignore("magicWord")
        #if self.dbg_running_fast:
        #    self.toggleRun()
        self.hidefont()
        DistributedObject.DistributedObject.disable(self)

    def setMagicWord(self, word, avId, zoneId):
        try:
            self.doMagicWord(word, avId, zoneId)
        except:
            response = PythonUtil.describeException(backTrace = 1)
            self.notify.warning("Ignoring error in magic word:\n%s" % response)
            self.setMagicWordResponse(response)

    def wordIs(self, word, w):
        return word == w or word[:(len(w)+1)] == ('%s ' % w)

    def getWordIs(self, word):
        # bind a word to self.wordIs and return a callable obj
        return Functor(self.wordIs, word)

    def doMagicWord(self, word, avId, zoneId):
        wordIs = self.getWordIs(word)

        print(word)
        if wordIs("~oobe"):
            base.oobe()
        elif wordIs("~oobeCull"):
            base.oobeCull()
        elif wordIs("~tex"):
            self.doTex(word)
        elif wordIs("~texmem"):
            base.toggleTexMem()
        elif wordIs("~verts"):
            base.toggleShowVertices()
        elif wordIs("~wire"):
            base.toggleWireframe()
        elif wordIs("~stereo"):
            base.toggleStereo()
        elif wordIs("~showfont"):
            self.showfont(word[9:])
        elif wordIs("~hidefont"):
            self.hidefont()
        elif wordIs("~guiPopup"):
            self.toggleGuiPopup()

        elif wordIs("~showCS") or wordIs("~showcs"):
            bitmask = self.getCSBitmask(word[7:])
            render.showCS(bitmask)
            self.csShown = 1

        elif wordIs("~hideCS") or wordIs("~hidecs"):
            bitmask = self.getCSBitmask(word[7:])
            render.hideCS(bitmask)
            self.csShown = 0

        elif wordIs("~cs"):
            # Toggle hide/show collision solids:
            # (Also a shorthand for ~hideCS and ~showCS).
            bitmask = self.getCSBitmask(word[3:])
            if self.csShown:
                render.hideCS(bitmask)
                self.csShown = 0
            else:
                render.showCS(bitmask)
                self.csShown = 1

        elif wordIs("~showShadowCollisions"):
            self.showShadowCollisions()

        elif wordIs("~hideShadowCollisions"):
            self.hideShadowCollisions()

        elif wordIs("~showCollisions"):
            self.showCollisions()

        elif wordIs("~hideCollisions"):
            self.hideCollisions()

        elif wordIs("~showCameraCollisions"):
            self.showCameraCollisions()

        elif wordIs("~hideCameraCollisions"):
            self.hideCameraCollisions()

        elif wordIs("~collidespam"):
            n = Notify.ptr().getCategory(':collide')
            if hasattr(self, '_collideSpamSeverity'):
                n.setSeverity(self._collideSpamSeverity)
                del self._collideSpamSeverity
            else:
                self._collideSpamSeverity = n.getSeverity()
                n.setSeverity(NSSpam)

        elif wordIs("~notify"):
            args = word.split()
            n = Notify.ptr().getCategory(args[1])
            n.setSeverity(
                {'error': NSError,
                 'warning': NSWarning,
                 'info': NSInfo,
                 'debug': NSDebug,
                 'spam': NSSpam,}[args[2]])

        # MPG we probably need generic versions of these
        #elif wordIs("~listen"):
        #    base.localAvatar.garbleChat = 0

        #elif wordIs("~nochat") or wordIs("~chat") or wordIs("~superchat"):
        #    base.localAvatar.garbleChat = 1

        elif wordIs("~stress"):
            factor = word[7:]
            if factor:
                factor = float(factor)
                LOD.setStressFactor(factor)
                response = "Set LOD stress factor to %s" % (factor)
            else:
                factor = LOD.getStressFactor()
                response = "LOD stress factor is %s" % (factor)

            self.setMagicWordResponse(response)

        elif wordIs("~for"):
            self.forAnother(word, avId, zoneId)

        elif wordIs("~badname"):
            # ~badname with an argument becomes ~for ... ~badname
            word = "~for %s ~badname" % (word[9:])
            print("word is %s" % (word))
            self.forAnother(word, avId, zoneId)

        elif wordIs('~avId'):
            self.setMagicWordResponse(str(localAvatar.doId))

        elif wordIs("~doId"):
            name = word[6:].strip()

            objs = self.identifyDistributedObjects(name)
            if (len(objs) == 0):
                response = "%s is unknown." % (name)
            else:
                response = ""
                for name, obj in objs:
                    response += "\n%s %d" % (name, obj.doId)
                response = response[1:]

            self.setMagicWordResponse(response)

        # MPG - need generic versions of these
        #elif wordIs("~collisions_on"):
        #    base.localAvatar.collisionsOn()

        #elif wordIs("~collisions_off"):
        #    base.localAvatar.collisionsOff()

        #elif wordIs('~addCameraPosition'):
        #    base.localAvatar.addCameraPosition()

        #elif wordIs('~removeCameraPosition'):
        #    base.localAvatar.removeCameraPosition()

        #elif wordIs('~printCameraPosition'):
        #    base.localAvatar.printCameraPosition(
        #        base.localAvatar.cameraIndex)

        #elif wordIs('~printCameraPositions'):
        #    base.localAvatar.printCameraPositions()

        elif wordIs("~exec"):
            # Enable execChat.
            from otp.chat import ChatManager
            ChatManager.ChatManager.execChat = 1

        elif wordIs("~run"):
            self.toggleRun()

        elif wordIs("~runFaster"):
            if(ConfigVariableBool("want-running",1).getValue()):
                args = word.split()
                if(len(args)>1):
                    base.debugRunningMultiplier = float(args[1])
                else:
                    base.debugRunningMultiplier = 10
                inputState.set("debugRunning", True)

        elif wordIs("~who"):
            # Get all the nearby avIds and send them to the AI.
            avIds = []
            for av in Avatar.Avatar.ActiveAvatars:
                # If the avatar has a friends list, it's probably a
                # real avatar and not an NPC.
                if hasattr(av, "getFriendsList"):
                    avIds.append(av.doId)
            self.d_setWho(avIds)

        elif wordIs("~sync"):
            # Sync with the AI, like F6, but rather than accumulating
            # sync informatoin, throw away whatever information was
            # there from before.  If a second parameter is supplied,
            # it is a number of seconds of temporary extra skew to
            # apply; the default is 0.

            tm = self.cr.timeManager
            if tm == None:
                response = "No TimeManager."
                self.setMagicWordResponse(response)
            else:
                tm.extraSkew = 0.0
                skew = word[5:].strip()
                if skew != "":
                    tm.extraSkew = float(skew)
                globalClockDelta.clear()
                tm.handleHotkey()

        elif wordIs("~period"):
            # Reset the period timer to expire in the indicated number
            # of seconds, or with no parameter, report the number of
            # seconds remaining.

            timeout = word[7:].strip()
            if timeout != "":
                seconds = int(timeout)
                self.cr.stopPeriodTimer()
                self.cr.resetPeriodTimer(seconds)
                self.cr.startPeriodTimer()

            # Now report the number of seconds remaining.
            if self.cr.periodTimerExpired:
                response = "Period timer has expired."

            elif self.cr.periodTimerStarted:
                elapsed = globalClock.getFrameTime() - self.cr.periodTimerStarted
                secondsRemaining = self.cr.periodTimerSecondsRemaining - elapsed
                response = "Period timer expires in %s seconds." % (int(secondsRemaining))
            else:
                response = "Period timer not set."

            self.setMagicWordResponse(response)

        elif wordIs("~DIRECT"):
            args = word.split()
            fEnableLight = 0
            if len(args) > 1:
                if direct and (args[1] == 'CAM'):
                    direct.enable()
                    taskMgr.removeTasksMatching('updateSmartCamera*')
                    camera.wrtReparentTo(render)
                    direct.cameraControl.enableMouseFly()
                    self.setMagicWordResponse("Enabled DIRECT camera")
                    return
                elif args[1] == 'LIGHT':
                    fEnableLight = 1
            # Start up DIRECT
            base.startTk()
            from direct.directtools import DirectSession
            if fEnableLight:
                direct.enableLight()
            else:
                direct.enable()
            self.setMagicWordResponse("Enabled DIRECT")

        elif wordIs("~TT"):
            if not direct:
                return
            args = word.split()
            if len(args) > 1:
                if (args[1] == 'CAM'):
                    direct.cameraControl.disableMouseFly()
                    camera.wrtReparentTo(base.localAvatar)
                    base.localAvatar.startUpdateSmartCamera()
                    self.setMagicWordResponse("Disabled DIRECT camera")
                    return
            # Return to toontown mode
            direct.disable()
            camera.wrtReparentTo(base.localAvatar)
            base.localAvatar.startUpdateSmartCamera()
            self.setMagicWordResponse("Disabled DIRECT")

        elif wordIs("~net"):
            # Simulate pulling or restoring the network plug.
            if self.cr.networkPlugPulled():
                self.cr.restoreNetworkPlug()
                self.cr.startHeartbeat()
                response = "Network restored."
            else:
                self.cr.pullNetworkPlug()
                self.cr.stopHeartbeat()
                response = "Network disconnected."
            self.setMagicWordResponse(response)

        elif wordIs('~disconnect'):
            # force a simulated disconnect
            # you can also do this from the OTP webpage
            base.cr.distributedDistrict.sendUpdate('broadcastMessage')

        elif wordIs("~model"):
            # load a model into the scene graph at the location of localAvatar
            args = word.split()
            path = args[1]
            model = loader.loadModel(path)
            model.reparentTo(localAvatar)
            model.wrtReparentTo(render)
            self.setMagicWordResponse('loaded %s' % path)

        elif wordIs("~axis"):
            # Show a 10 foot and 100 foot axis at the spot of the avatar
            # axis aligned to render
            axis = loader.loadModel("models/misc/xyzAxis.bam")
            axis.reparentTo(render)
            axis.setPos(base.localAvatar, 0,0,0)
            axis.setHpr(render, 0,0,0)
            axis10 = loader.loadModel("models/misc/xyzAxis.bam")
            axis10.reparentTo(render)
            axis10.setPos(base.localAvatar, 0,0,0)
            axis10.setScale(10)
            axis10.setHpr(render, 0,0,0)
            axis10.setColorScale(1,1,1,0.4)
            axis10.setTransparency(1)

        elif (wordIs("~clearAxes") or wordIs("~clearAxis")):
            # Remove the effects of ~axis calls
            render.findAllMatches("**/xyzAxis.egg").detach()

        elif wordIs("~myAxis"):
            if hasattr(self, 'myAxis'):
                self.myAxis.detachNode()
                del self.myAxis
            else:
                self.myAxis = loader.loadModel("models/misc/xyzAxis.bam")
                self.myAxis.reparentTo(localAvatar)

        elif (wordIs("~osd")):
            onScreenDebug.enabled = not onScreenDebug.enabled

        elif wordIs("~osdScale"):
            args = word.split()
            defScale = .05
            if len(args) > 1:
                scale = float(args[1])
            else:
                scale = 1.
            onScreenDebug.onScreenText.setScale(defScale * scale)

        elif wordIs('~osdTaskMgr'):
            if taskMgr.osdEnabled():
                taskMgr.stopOsd()
            else:
                if not onScreenDebug.enabled:
                    onScreenDebug.enabled = True
                taskMgr.startOsd()

        elif wordIs("~fps"):
            self.doFps(word, avId, zoneId)

        elif wordIs("~sleep"):
            args = word.split()
            if len(args) > 1:
                s = float(args[1])
                base.setSleep(s)
                response = 'sleeping %s' % s
            else:
                base.setSleep(0.0)
                response = 'not sleeping'
            self.setMagicWordResponse(response)

        elif wordIs('~objects'):
            args = word.split()
            from direct.showbase import ObjectReport
            report = ObjectReport.ObjectReport('client ~objects')

            if 'all' in args:
                self.notify.info('printing full object set...')
                report.getObjectPool().printObjsByType() #(printReferrers='ref' in args)

            if hasattr(self, 'baselineObjReport'):
                self.notify.info('calculating diff from baseline ObjectReport...')
                self.lastDiff = self.baselineObjReport.diff(report)
                self.lastDiff.printOut(full=('diff' in args or 'dif' in args))

            if 'baseline' in args or not hasattr(self, 'baselineObjReport'):
                self.notify.info('recording baseline ObjectReport...')
                if hasattr(self, 'baselineObjReport'):
                    self.baselineObjReport.destroy()
                self.baselineObjReport = report

            self.setMagicWordResponse('objects logged')
        
        elif wordIs('~objectcount'):
            def handleObjectCountDone(objectCount):
                self.setMagicWordResponse('object count logged')
                oc = ObjectCount('~objectcount', doneCallback=handleObjectCountDone)

        elif wordIs('~objecthg'):
            import gc
            objs = gc.get_objects()
            type2count = {}
            for obj in objs:
                tn = safeTypeName(obj)
                type2count.setdefault(tn, 0)
                type2count[tn] += 1
            count2type = invertDictLossless(type2count)
            counts = list(count2type.keys())
            counts.sort()
            counts.reverse()
            for count in counts:
                print('%s: %s' % (count, count2type[count]))
            self.setMagicWordResponse('~aiobjecthg complete')

        elif wordIs('~containers'):
            args = word.split()
            limit = 30
            if 'full' in args:
                limit = None
            ContainerReport.ContainerReport('~containers', log=True, limit=limit, threaded=True)

        elif wordIs('~garbage'):
            args = word.split()
            # it can take a LOOONG time to print out the garbage referrers and referents
            # by reference (as opposed to by number)
            full = 'full' in args
            safeMode = 'safe' in args
            delOnly = 'delonly' in args
            cycleLimit = None
            for arg in args:
                try:
                    cycleLimit = int(arg)
                    break
                except:
                    pass
            # This does a garbage collection and dumps the list of leaked (uncollectable) objects to the log.
            GarbageReport.GarbageLogger('~garbage', fullReport=full, threaded=True,
                                        safeMode=safeMode, delOnly=delOnly,
                                        doneCallback=self.garbageReportDone)
            # this is coming back from the AI
            #self.setMagicWordResponse('garbage logged')

        elif wordIs('~guicreates'):
            base.printGuiCreates = True
            self.setMagicWordResponse('printing gui creation stacks')

        elif wordIs("~creategarbage"):
            args = word.split()
            num = 1
            if len(args) > 1:
                num = int(args[1])
            GarbageReport._createGarbage(num)
            # this is coming back from the AI
            #self.setMagicWordResponse(senderId, 'leaked garbage created')

        elif wordIs('~leakTask'):
            def leakTask(task):
                return task.cont
            taskMgr.add(leakTask, uniqueName('leakedTask'))
            leakTask = None
            # this is coming back from the AI
            #self.setMagicWordResponse(senderId, 'leaked task created')

        elif wordIs('~leakmessage'):
            MessengerLeakDetector._leakMessengerObject()
            self.down_setMagicWordResponse(senderId, 'messenger leak object created')

        elif wordIs('~pstats'):
            args = word.split()
            hostname = None
            port = None
            if len(args) > 1:
                hostname = args[1]
            if len(args) > 2:
                port = int(args[2])
            # make sure pstats is enabled
            base.wantStats = 1
            Task.TaskManager.pStatsTasks = 1
            result = base.createStats(hostname, port)
            connectionName = '%s' % hostname
            if port is not None:
                connectionName += ':%s' % port
            if result:
                response = 'connected client pstats to %s' % connectionName
            else:
                response = 'could not connect pstats to %s' % connectionName
            self.setMagicWordResponse(response)

        elif wordIs('~profile'):
            args = word.split()
            if len(args) > 1:
                num = int(args[1])
            else:
                num = 5
            session = taskMgr.getProfileSession('~profile')
            session.setLogAfterProfile(True)
            taskMgr.profileFrames(num, session)
            self.setMagicWordResponse('profiling %s client frames...' % num)

        elif wordIs('~frameprofile'):
            args = word.split()
            wasOn = bool(taskMgr.getProfileFrames())
            if len(args) > 1:
                setting = bool(int(args[1]))
            else:
                setting = not wasOn
            taskMgr.setProfileFrames(setting)
            self.setMagicWordResponse(
                'frame profiling %s%s' % (choice(setting, 'ON', 'OFF'),
                                        choice(wasOn == setting, ' already', '')))

        elif wordIs('~taskprofile'):
            args = word.split()
            wasOn = bool(taskMgr.getProfileTasks())
            if len(args) > 1:
                setting = bool(int(args[1]))
            else:
                setting = not wasOn
            taskMgr.setProfileTasks(setting)
            self.setMagicWordResponse(
                'task profiling %s%s' % (choice(setting, 'ON', 'OFF'),
                                       choice(wasOn == setting, ' already', '')))

        elif wordIs('~taskspikethreshold'):
            args = word.split()
            if len(args) > 1:
                threshold = float(args[1])
                response = 'task spike threshold set to %ss' % threshold
            else:
                threshold = TaskProfiler.GetDefaultSpikeThreshold()
                response = 'task spike threshold reset to %ss' % threshold
            TaskProfiler.SetSpikeThreshold(threshold)
            self.setMagicWordResponse(response)

        elif wordIs('~logtaskprofiles'):
            args = word.split()
            if len(args) > 1:
                name = args[1]
            else:
                name = None
            taskMgr.logTaskProfiles(name)
            response = 'logged task profiles%s' % choice(name, ' for %s' % name, '')
            self.setMagicWordResponse(response)

        elif wordIs('~taskprofileflush'):
            args = word.split()
            if len(args) > 1:
                name = args[1]
            else:
                name = None
            taskMgr.flushTaskProfiles(name)
            response = 'flushed AI task profiles%s' % choice(name, ' for %s' % name, '')
            self.setMagicWordResponse(response)

        elif wordIs('~dobjectcount'):
            base.cr.printObjectCount()
            self.setMagicWordResponse('logging client distributed object count...')

        elif wordIs('~taskmgr'):
            print(taskMgr)
            self.setMagicWordResponse('logging client taskMgr...')

        elif wordIs('~jobmgr'):
            print(jobMgr)
            self.setMagicWordResponse('logging client jobMgr...')

        elif wordIs('~jobtime'):
            args = word.split()
            if len(args) > 1:
                time = float(args[1])
            else:
                time = None
            response = ''
            if time is None:
                time = jobMgr.getDefaultTimeslice()
                response = 'reset client jobMgr timeslice to %s ms' % time
            else:
                response = 'set client jobMgr timeslice to %s ms' % time
                time = time / 1000.
            jobMgr.setTimeslice(time)
            self.setMagicWordResponse(response)

        elif wordIs('~detectleaks'):
            started = self.cr.startLeakDetector()
            self.setMagicWordResponse(
                choice(started,
                       'leak detector started',
                       'leak detector already started',
                       ))

        elif wordIs('~taskthreshold'):
            args = word.split()
            if len(args) > 1.:
                threshold = float(args[1])
            else:
                threshold = None
            response = ''
            if threshold is None:
                threshold = taskMgr.DefTaskDurationWarningThreshold
                response = 'reset task duration warning threshold to %s' % threshold
            else:
                response = 'set task duration warning threshold to %s' % threshold
            taskMgr.setTaskDurationWarningThreshold(threshold)
            self.setMagicWordResponse(response)

        elif wordIs('~messenger'):
            print(messenger)
            self.setMagicWordResponse('logging client messenger...')

        elif wordIs('~clientcrash'):
            # if we call notify.error directly, the magic word mgr will catch it
            # self.notify.error doesn't seem to work either
            DelayedCall(Functor(self.notify.error, '~clientcrash: simulating a client crash'))

        elif wordIs('~badDelete'):
            doId = 0
            while doId in base.cr.doId2do:
                doId += 1
            # location (0,0) is special, pass in (1,1)
            # deleteObjectLocation expects a DO, pass in a ScratchPad instead
            # we must delay the call because magicWordMgr is in a big try/except block
            DelayedCall(Functor(base.cr.deleteObjectLocation, ScratchPad(doId=doId), 1, 1))
            self.setMagicWordResponse('doing bad delete')

        elif wordIs("~idTags"):
            messenger.send('nameTagShowAvId', [])
            base.idTags = 1

        elif wordIs("~nameTags"):
            messenger.send('nameTagShowName', [])
            base.idTags = 0

        elif wordIs("~hideNames"):
            # note do ~hideNames before ~hideGui if you want both off
            if NametagGlobals.getMasterNametagsVisible():
                NametagGlobals.setMasterNametagsVisible(0)
            else:
                NametagGlobals.setMasterNametagsVisible(1)

        elif wordIs("~hideGui"):
            if aspect2d.isHidden():
                aspect2d.show()
            else:
                aspect2d.hide()

        elif wordIs('~flush'):
            base.cr.doDataCache.flush()
            base.cr.cache.flush()
            self.setMagicWordResponse('client object and data caches flushed')

        elif wordIs('~prof'):
            import time

            ### set up ###
            name = 'default'
            p = Point3()
            ##############

            ts = time.time()
            for i in range(1000000):

                ### code to be timed ###
                p.set(1,2,3)
                ########################

            tf = time.time()
            dt = tf - ts
            response = 'prof(%s): %s secs' % (name, dt)
            print(response)
            self.setMagicWordResponse(response)

        elif wordIs('~gptc'):
            args = word.split()
            if len(args) > 1. and hasattr(self.cr, 'leakDetector'):
                gptcJob = self.cr.leakDetector.getPathsToContainers(
                    '~gptc', args[1], Functor(self._handleGPTCfinished, args[1]))
            else:
                self.setMagicWordResponse('error')

        elif wordIs('~gptcn'):
            args = word.split()
            if len(args) > 1. and hasattr(self.cr, 'leakDetector'):
                gptcnJob = self.cr.leakDetector.getPathsToContainersNamed(
                    '~gptcn', args[1], Functor(self._handleGPTCNfinished, args[1]))
            else:
                self.setMagicWordResponse('error')
 
        #elif wordIs('~ls'):
        #    base.render.ls()

        #elif wordIs('~lsLocalAvatar'):
        #    base.localAvatar.ls()

        else:
            # Not a magic word I know!
            return 0

        return 1

    # MPG need a generic version of this
    def toggleRun(self):
        if(ConfigVariableBool("want-running",1).getValue()):
            inputState.set("debugRunning",
                           inputState.isSet("debugRunning") != True)

    def d_setMagicWord(self, magicWord, avId, zoneId):
        self.sendUpdate("setMagicWord", [magicWord, avId, zoneId,
                                         base.cr.userSignature])

    def b_setMagicWord(self, magicWord, avId = None, zoneId = None):
        print("b_setMagicWord")
        if self.cr.wantMagicWords:
            print("We want magic words")
            if avId == None:
                avId = base.localAvatar.doId

            if zoneId == None:
                # Try to figure out what zone the avatar is in.  Some
                # magic words find this useful.
                try:
                    zoneId = self.cr.playGame.getPlace().getZoneId()
                except:
                    pass
                if zoneId == None:
                    zoneId = 0

            self.d_setMagicWord(magicWord, avId, zoneId)

            # We handle this as a special case, before we get into
            # setMagicWord, since that function will trap exceptions.
            if (magicWord.count('~crash')):
                args = magicWord.split()
                errorCode = 12 # 12 = general python exception
                if len(args) > 1:
                    errorCode = int(args[1])

                self.notify.info("Simulating client crash: exit error = %s" % (errorCode))
                base.exitShow(errorCode)

            if (magicWord.count('~exception')):
                self.notify.error('~exception: simulating a client exception...')
                s = ''
                while 1:
                    s += 'INVALIDNAME'
                    eval(s)

            self.setMagicWord(magicWord, avId, zoneId)


    def setMagicWordResponse(self, response):
        """setMagicWordResponse(self, string response)

        The AI might send a formatted string response to certain magic
        words.
        """
        self.notify.info(response)
        base.localAvatar.setChatAbsolute(response, CFSpeech | CFTimeout)
        base.talkAssistant.receiveDeveloperMessage(response)

    def d_setWho(self, avIds):
        self.sendUpdate("setWho", [avIds])

    def _handleGPTCfinished(self, ct, gptcJob):
        self.setMagicWordResponse('gptc(%s) finished' % ct)

    def _handleGPTCNfinished(self, cn, gptcnJob):
        self.setMagicWordResponse('gptcn(%s) finished' % cn)

    def forAnother(self, word, avId, zoneId):
        # The magic word ~for was spoken, which means to execute the
        # rest of the string as a magic word on behalf on another
        # avatar.

        # Separate out the next magic word and the name.
        b = 5
        while word[b:b+2] != ' ~':
            b += 1
            if b >= len(word):
                self.setMagicWordResponse("No next magic word!")
                return

        nextWord = word[b+1:]
        name = word[5:b].strip()

        id = self.identifyAvatar(name)
        if (id == None):
            self.setMagicWordResponse("Don't know who %s is." % (name))
            return

        self.d_setMagicWord(nextWord, id, zoneId)

    def identifyAvatar(self, name):
        self.notify.error("Pure virtual - please override me.")

    def identifyDistributedObjects(self, name):
        # Find the nearby distributed object or objects (of any type)
        # with the given name.  Returns a list of (name, obj) pairs.

        result = []
        lowerName = name.lower()

        for obj in list(self.cr.doId2do.values()):
            className = obj.__class__.__name__
            try:
                name = obj.getName()
            except:
                name = className

            if name.lower() == lowerName or \
               className.lower() == lowerName or \
               className.lower() == "distributed" + lowerName:
                result.append((name, obj))

        return result

    def doTex(self, word):
        """ Toggles texturing (with no parameters) or shows the named
        texture (with a parameter). """

        args = word.split()
        if len(args) <= 1:
            # No parameters: clean up the old texture viewer.
            if self.texViewer:
                self.texViewer.cleanup()
                self.texViewer = None
                return

            # No parameters, and now texture viewer: toggle texture.
            base.toggleTexture()
            return

        # At least one parameter: show the named texture.
        if self.texViewer:
            self.texViewer.cleanup()
            self.texViewer = None

        tex = TexturePool.findTexture(args[1])
        if not tex:
            # Try it with stars on both ends.
            tex = TexturePool.findTexture('*%s*' % (args[1]))

        if not tex:
            # Couldn't find that texture.
            self.setMagicWordResponse("Unknown texture: %s" % (args[1]))
            return

        self.texViewer = TexViewer(tex)

    def getCSBitmask(self, st):
        # Decompose the string into keywords, and return the
        # corresponding collision bitmask, suitable for passing to
        # NodePath.showCS() or hideCS().
        words = st.lower().split()
        if len(words) == 0:
            return None

        invalid = ""

        bitmask = BitMask32.allOff()
        for w in words:
            if w == "wall":
                bitmask |= OTPGlobals.WallBitmask
            elif w == "floor":
                bitmask |= OTPGlobals.FloorBitmask
            elif w == "cam":
                bitmask |= OTPGlobals.CameraBitmask
            elif w == "catch":
                bitmask |= OTPGlobals.CatchBitmask
            elif w == "ghost":
                bitmask |= OTPGlobals.GhostBitmask
            elif w == "pet":
                bitmask |= OTPGlobals.PetBitmask
            elif w == "furniture":
                bitmask |= (OTPGlobals.FurnitureSideBitmask |
                            OTPGlobals.FurnitureTopBitmask |
                            OTPGlobals.FurnitureDragBitmask)
            elif w == "furnitureside":
                bitmask |= OTPGlobals.FurnitureSideBitmask
            elif w == "furnituretop":
                bitmask |= OTPGlobals.FurnitureTopBitmask
            elif w == "furnituredrag":
                bitmask |= OTPGlobals.FurnitureDragBitmask
            elif w == "pie":
                bitmask |= OTPGlobals.PieBitmask
            else:
                try:
                    # Convert the string to an integer and use that
                    # to spec a bitmask. Use try/except because w
                    # might not be an integer. Is there a better way
                    # to check?
                    bitmask |= BitMask32.bit(int(w))
                    print(bitmask)
                except ValueError:
                    invalid += " " + w
        if invalid:
            self.setMagicWordResponse("Unknown CS keyword(s): %s" % invalid)

        return bitmask

    def getFontByName(self, fontname):
        if fontname == "default":
            return TextNode.getDefaultFont()
        elif fontname == "interface":
            return OTPGlobals.getInterfaceFont()
        elif fontname == "sign":
            return OTPGlobals.getSignFont()
        else:
            return None

    def showfont(self, fontname):
        fontname = fontname.lower().strip()
        font = self.getFontByName(fontname)
        if font == None:
            self.setMagicWordResponse("Unknown font: %s" % (fontname))
            return

        if not isinstance(font, DynamicTextFont):
            self.setMagicWordResponse("Font %s is not dynamic." % (fontname))
            return

        # Hide the previously shown font, if any
        self.hidefont()

        # Show the new font.
        self.shownFontNode = aspect2d.attachNewNode('shownFont')

        # We use a TextNode just to create big square polygons.
        tn = TextNode('square')
        tn.setCardActual(0.0, 1.0, -1.0, 0.0)
        tn.setFrameActual(0.0, 1.0, -1.0, 0.0)
        tn.setCardColor(1, 1, 1, 0.5)
        tn.setFrameColor(1, 1, 1, 1)
        tn.setFont(font)
        tn.setText(' ')

        numXPages = 2
        numYPages = 2
        pageScale = 0.8
        pageMargin = 0.1

        numPages = font.getNumPages()
        x = 0
        y = 0
        for pi in range(numPages):
            page = font.getPage(pi)
            tn.setCardTexture(page)
            np = self.shownFontNode.attachNewNode(tn.generate())
            np.setScale(pageScale)
            np.setPos(float(x) / numXPages * 2 - 1 + pageMargin, 0,
                      1 - float(y) / numYPages * 2 - pageMargin),
            x += 1
            if x >= numXPages:
                y += 1
                x = 0

    def hidefont(self):
        if self.shownFontNode != None:
            self.shownFontNode.removeNode()
            self.shownFontNode = None

    def showShadowCollisions(self):
        try:
            base.shadowTrav.showCollisions(render)
        except:
            self.setMagicWordResponse("CollisionVisualizer is not compiled in.")

    def hideShadowCollisions(self):
        base.shadowTrav.hideCollisions()

    def showCollisions(self):
        try:
            base.cTrav.showCollisions(render)
        except:
            self.setMagicWordResponse("CollisionVisualizer is not compiled in.")

    def hideCollisions(self):
        base.cTrav.hideCollisions()

    def showCameraCollisions(self):
        try:
            localAvatar.ccTrav.showCollisions(render)
        except:
            self.setMagicWordResponse("CollisionVisualizer is not compiled in.")

    def hideCameraCollisions(self):
        localAvatar.ccTrav.hideCollisions()

    def doFps(self, word, avId, zoneId):
        # The ~fps magic word: play with the frame rate meter and the
        # funny clock modes.

        args = word.split()

        response = None
        if len(args) == 1 or args[1] == "normal":
            # ~fps or ~fps normal: toggle the frame rate meter and/or
            # return the clock to normal mode.

            if globalClock.getMode() != ClockObject.MNormal:
                globalClock.setMode(ClockObject.MNormal)
                response = "Normal frame rate set."
            else:
                base.setFrameRateMeter(not base.frameRateMeter)

        elif args[1] == "forced":
            # ~fps forced fps: force a particular frame rate.
            fps = float(args[2])
            globalClock.setMode(ClockObject.MForced)
            globalClock.setDt(1.0/fps)
            response = "Frame rate forced to %s fps." % (fps)
            base.setFrameRateMeter(1)

        elif args[1] == "degrade":
            # ~fps degrade factor: degrade the frame rate by the
            # indicated factor.
            factor = float(args[2])
            globalClock.setMode(ClockObject.MDegrade)
            globalClock.setDegradeFactor(factor)
            response = "Frame rate degraded by factor of %s." % (factor)
            base.setFrameRateMeter(1)

        elif args[1][-1] == '%':
            # ~fps <x>%: degrade the frame rate to the indicated
            # percentage.
            percent = float(args[1][:-1])
            if (percent == 100):
                globalClock.setMode(ClockObject.MNormal)
                response = "Normal frame rate set."
            else:
                globalClock.setMode(ClockObject.MDegrade)
                globalClock.setDegradeFactor(100.0/percent)
                response = "Frame rate degraded to %s percent." % (percent)
            base.setFrameRateMeter(1)

        else:
            try:
                fps = float(args[1])
            except:
                fps = None
            if fps != None:
                # ~fps <x>: force a particular frame rate.
                globalClock.setMode(ClockObject.MForced)
                globalClock.setDt(1.0/fps)
                response = "Frame rate forced to %s fps." % (fps)
                base.setFrameRateMeter(1)
            else:
                response = "Unknown fps command: ~s" % (args[1])

        if base.frameRateMeter:
            # Restore the average frame rate interval to a sensible
            # value for display the fps meter.  This might have been
            # set too high by the client-fps mechanism.
            globalClock.setAverageFrameRateInterval(ConfigVariableDouble('average-frame-rate-interval').getValue())

        if response != None:
            self.setMagicWordResponse(response)


    def identifyAvatar(self, name):
        # Find the nearby avatar with the given name.

        # First, try an exact name match.
        for av in Avatar.Avatar.ActiveAvatars:
            if isinstance(av, self.GameAvatarClass) and \
               av.getName() == name:
                return av.doId

        # No good; try a case-insensitive match.
        lowerName = name.lower()
        for av in Avatar.Avatar.ActiveAvatars:
            if isinstance(av, self.GameAvatarClass) and \
               av.getName().lower().strip() == lowerName:
                return av.doId

        # Is it a doId anyway?
        try:
            avId = int(name)
            return avId
        except:
            pass

        # Oh well.
        return None

    def toggleGuiPopup(self):
        if self.guiPopupShown:
            base.mouseWatcherNode.hideRegions()
            self.guiPopupShown = 0
        else:
            base.mouseWatcherNode.showRegions(render2d, 'gui-popup', 0)
            self.guiPopupShown = 1

    def garbageReportDone(self, garbageReport):
        self.setMagicWordResponse('%s garbage cycles' % garbageReport.getNumCycles())

def magicWord(mw):
    messenger.send('magicWord', [mw])

import builtins
builtins.magicWord = magicWord
