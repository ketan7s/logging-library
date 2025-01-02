from abc import ABC, abstractmethod
from threading import Thread, Lock
from queue import Queue
import os
import gzip

class Sink(ABC):
    @abstractmethod
    def write(self, message: str):
        pass

class FileSink(Sink):
    def __init__(self, config):
        self.file_location = config.file_location
        self.max_file_size = config.max_file_size
        self.write_mode = config.write_mode
        self.lock = Lock() if config.thread_model == "SINGLE" else None
        self.queue = Queue() if self.write_mode == "ASYNC" else None

        if self.write_mode == "ASYNC":
            self._start_async_writer()

    def _start_async_writer(self):
        self.async_thread = Thread(target=self._process_queue)
        self.async_thread.daemon = True
        self.async_thread.start()

    def _process_queue(self):
        while True:
            message = self.queue.get()
            if message is None:
                break
            self._write_to_file(message)

    def write(self, message: str):
        if self.write_mode == "ASYNC":
            self.queue.put(message)
        else:
            self._write_to_file(message)

    def _write_to_file(self, message: str):
        if self.lock:
            with self.lock:
                self._write_message_with_rotation(message)
        else:
            self._write_message_with_rotation(message)

    def _write_message_with_rotation(self, message: str):
        self._rotate_file_if_needed()
        with open(self.file_location, "a") as f:
            f.write(message + "\n")

    def _rotate_file_if_needed(self):
        if os.path.exists(self.file_location) and os.path.getsize(self.file_location) >= self.max_file_size:
            base, ext = os.path.splitext(self.file_location)
            rotated_file = f"{base}.1{ext}"

            os.rename(self.file_location, rotated_file)

            if os.path.exists(rotated_file):
                with open(rotated_file, "rb") as f_in:
                    with gzip.open(f"{rotated_file}.gz", "wb") as f_out:
                        f_out.writelines(f_in)

                os.remove(rotated_file)


class DatabaseSink(Sink):
    def __init__(self, config):
        self.db_config = config

    def write(self, message: str):
        pass

class ConsoleSink(Sink):
    def __init__(self, config):
        self.console_config = config

    def write(self, message: str):
        print(f"ConsoleSink: {message}")
