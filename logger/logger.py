from datetime import datetime
from threading import Lock

from .message import Message
from .sinks import FileSink, DatabaseSink, ConsoleSink
from .config import Config

class Logger:
    LEVELS = ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]

    def __init__(self, config: Config):
        self.config = config
        self.sinks = self._initialize_sinks(config)
        self.lock = Lock() if config.thread_model == "SINGLE" else None

    def _initialize_sinks(self, config: Config):
        sinks = []
        if config.sink_type == "FILE":
            sinks.append(FileSink(config))
        elif config.sink_type == "DB":
            sinks.append(DatabaseSink(config))
        elif config.sink_type == "CONSOLE":
            sinks.append(ConsoleSink(config))
        return sinks

    def log(self, message: Message):
        if message.level not in self.LEVELS:
            raise ValueError(f"Invalid log level: {message.level}")

        if self.LEVELS.index(message.level) < self.LEVELS.index(self.config.log_level):
            return

        log_message = self._format_message(message)

        for sink in self.sinks:
            try:
                sink.write(log_message)
            except Exception as e:
                print(f"Error writing to sink: {e}")

    def _format_message(self, message: Message):
        timestamp = datetime.now().strftime(self.config.ts_format)
        return (f"{message.level} [{timestamp}] [{message.namespace}] {message.content} "
                f"(tracking_id={message.tracking_id}, hostname={message.hostname})")

