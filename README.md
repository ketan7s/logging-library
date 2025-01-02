# Logger Implementation

This project implements a configurable logging framework that supports multiple sink types (e.g., File, Console, Database), threading models, and log rotation.

## Features

- **Configurable Log Levels:** Supports `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL`.
- **Sink Types:** Write logs to file, console, or database.
- **Threading Models:** Choose between `SINGLE` (thread-safe) or `MULTI` threading.
- **Write Modes:** Synchronous (`SYNC`) or Asynchronous (`ASYNC`) logging.
- **Log Rotation:** Automatically rotates and compresses logs when file size exceeds the limit.
- **Customizable Timestamps:** Specify timestamp format for log entries.

## Project Structure

```plaintext
.
├── logger/
│   ├── __init__.py
│   ├── config.py          # Handles configuration for the logger.
│   ├── logger.py          # Main logging implementation.
│   ├── message.py         # Defines the Message class for log entries.
│   ├── sinks.py           # Sink implementations (FileSink, ConsoleSink, DatabaseSink).
├── tests/
│   ├── test_logger.py     # Test script for logging functionality.
│   ├── read_compressed_log.py # Utility to read compressed log files.
└── README.md              # Project documentation.
