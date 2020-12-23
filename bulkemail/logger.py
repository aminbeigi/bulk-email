import logging

"""logger"""

LOGGING_FILE_PATH = 'logs/bulkemail.log'

class Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('src/logging/test.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] %(name)s %(levelname)s (%(funcName)s) %(message)s')
    logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)

    @classmethod
    def get_logger(cls):
        return cls.logger