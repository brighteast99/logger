import logging
import logging.handlers

from .handlers import FileHandler


def setup_logger(
    name=None,
    log_dir="/",
    log_level=logging.DEBUG,
    logfile_level=logging.WARNING,
    log_format="%(message)s",
    logfile_format="%Y-%m-%d %H:%M:%S",
):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = FileHandler(log_dir, logfile_format)

    console_handler.setLevel(log_level)
    file_handler.setLevel(logfile_level)

    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
