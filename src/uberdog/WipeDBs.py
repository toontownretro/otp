import pymysql as MySQLdb
import direct
from otp.otpbase.OTPModules import *

config = getConfigShowbase()

username = ConfigVariableString("mysql-user")
password = ConfigVariableString("mysql-passwd")
dbSalt = ConfigVariableString("dev-branch-flavor","").getValue()
if dbSalt:
    dbSalt = dbSalt + '_'
    pass

if username == "" or password == "":
    print("Username or password not found, check your config.prc!")
    sys.exit(2)


db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=username,
                     passwd=password)

print("Connected to MySQL at localhost.")

cursor = db.cursor()

def dropdb(dbname):
    try:
        print("Dropping database %s:" % dbname)
        cursor.execute("DROP DATABASE %s"%dbname)
        print("  Success!")
    except Exception as e:
        print("  Failed: %s" % e)

dropdb("%savatar_accessories" % (dbSalt,))
dropdb("%savatar_friends" % (dbSalt,)) #
dropdb("%savatars" % (dbSalt,)) #
dropdb("%sawards" % (dbSalt,))
dropdb("%scode_redemption" % (dbSalt,))
dropdb("%sguilds" % (dbSalt,)) #
dropdb("%sholidayschedules" % (dbSalt,))
dropdb("%sstatus" % (dbSalt,))

db.commit()
