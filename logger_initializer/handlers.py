import logging
import os
from datetime import datetime


class FileHandler(logging.Handler):
    def __init__(self, log_dir, filename_format):
        super().__init__()

        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.filename_format = filename_format

    def emit(self, record):
        if record.levelno >= self.level:
            log_entry = self.format(record)
            log_filename = datetime.now().strftime(self.filename_format) + ".txt"
            log_filepath = os.path.join(self.log_dir, log_filename)
            with open(log_filepath, "a") as log_file:
                log_file.write(f"{log_entry}\n")
