"""
Start the UberDog (Uber Distributed Object Globals server).
"""

---------------------------
This is here to be a syntax error :) This is really an example Start.py
and not a .py file that you should be calling.  Look in the toontown,
gateway, or pirates directories for a ./src/uberdog/Start.py.

If you're starting a new project, you may want to copy this and remove
this instructional text and create your own foo.uberdog.Start.
---------------------------

class game:
    name = "uberDog"
    process = "server"
__builtins__["game"] = game()

import time
import os
import sys

# Initialize ihooks importer On the production servers, we run genPyCode -n
# meaning no squeeze, so nobody else does this. When we squeeze, the
# unpacker does this for us and it does not hurt to do in either case.
import ihooks
ihooks.install()

print("Initializing the UberDog (Uber Distributed Object Globals server)...")

from otp.uberdog.UberDogGlobal import *
from otp.uberdog.UberDog import UberDog
from direct.showbase.PythonUtil import *

uber.mdip = ConfigVariableString("msg-director-ip", "localhost").getValue()

uber.mdport = ConfigVariableInt("msg-director-port", 6666).getValue()

uber.esip = ConfigVariableString("event-server-ip", "localhost").getValue()
uber.esport = ConfigVariableInt("event-server-port", 4343).getValue()

serverId = ConfigVariableInt("district-ssid", 20100000).getValue()
uberDogMinChannel = ConfigVariableInt("uberdog-min-channel", 200400000).getValue()
uberDogMaxChannel = ConfigVariableInt("uberdog-max-channel", 200449999).getValue()

uber.air = UberDog(
        uber.mdip,
        uber.mdport,
        uber.esip,
        uber.esport,
        serverId,
        uberDogMinChannel,
        uberDogMaxChannel)

# How we let the world know we are not running a service
uber.aiService = 0

try:
    uber.air.fsm.request("districtReset")
    uber.air.fsm.request("playGame")
    run()
except:
    info = describeException()
    uber.air.writeServerEvent('uberdog-exception', 1, info)
    raise
