class Config:
    def __init__(self, config_dict):
        self.ts_format = config_dict.get("ts_format", "%d-%m-%Y %H:%M:%S")
        self.log_level = config_dict.get("log_level", "INFO")
        self.sink_type = config_dict.get("sink_type", "FILE")
        self.file_location = config_dict.get("file_location", "app.log")
        self.max_file_size = config_dict.get("max_file_size", 10 * 1024 * 1024)
        self.thread_model = config_dict.get("thread_model", "SINGLE")
        self.write_mode = config_dict.get("write_mode", "SYNC")
