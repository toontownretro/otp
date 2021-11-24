import direct
from otp.otpbase.OTPModules import *

class DBInterface:

    @classmethod
    def processDBName(cls, dbString):
        if __dev__:
            config = getConfigShowbase()
            dbSalt = ConfigVariableString("dev-branch-flavor","").getValue()
            if dbSalt:
                dbString = dbSalt + '_' + dbString
                pass
            pass
        return dbString

    def getErrorCode(self, exception):
        # returns error code from MySQL exception
        errStr = str(exception)
        commaIndex = errStr.index(',')
        codeStr = errStr[1:commaIndex]
        return int(codeStr)
