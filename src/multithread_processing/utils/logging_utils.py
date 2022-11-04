import logging
from logging.handlers import RotatingFileHandler

FORMATTER = logging.Formatter(
    fmt='[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
    datefmt='%m-%d-%Y %H:%M:%S %Z'
)
LOG_FILE = 'logging.log'


def get_console_handler():
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(filename=LOG_FILE):
    file_handler = RotatingFileHandler(filename, maxBytes=2000, backupCount=1)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name, filename=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    if filename is None:
        handler = get_console_handler()
    else:
        handler = get_file_handler(filename)
    logger.addHandler(handler)
    return logger
