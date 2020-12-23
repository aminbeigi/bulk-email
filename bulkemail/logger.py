import logging

"""logger"""

LOGGING_FILE_PATH = 'logs/bulkemail.log'

class Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOGGING_FILE_PATH)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] %(name)s %(levelname)s %(message)s')
    logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)

    @classmethod
    def getLogger(cls):
        return cls.logger