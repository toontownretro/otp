from mariadb.constants.ERR import *
from mariadb import (
    DataError,
    DatabaseError,
    Error,
    IntegrityError,
    InterfaceError,
    InternalError,
    NotSupportedError,
    OperationalError,
    PoolError,
    ProgrammingError,
    Warning,
)

DbAlreadyExists = ER_DB_CREATE_EXISTS
TableAlreadyExists = ER_TABLE_EXISTS_ERROR
ServerShuttingDown = ER_SERVER_SHUTDOWN
ServerGoneAway = CR_SERVER_GONE_ERROR
ServerLost = CR_SERVER_LOST