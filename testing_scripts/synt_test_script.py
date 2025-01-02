# import os
from logger.config import Config
from logger.logger import Logger
from logger.message import Message

config_dict = {
    "ts_format": "%d-%m-%Y %H:%M:%S",
    "log_level": "INFO",
    "sink_type": "FILE",
    "file_location": "test_sync.log",
    "thread_model": "MULTI",
    "write_mode": "ASYNC"
}

config = Config(config_dict)
logger = Logger(config)

for i in range(0, 1000):
    logger.log(Message(f"This is a test logging message {i}",
                       "INFO",
                       "TEST-1"))

with open("test_sync.log", "r") as f:
    lines = f.readlines()

print("Test Sync Log Output:")
for line in lines:
    print(line)

# os.remove("test_sync.log")
