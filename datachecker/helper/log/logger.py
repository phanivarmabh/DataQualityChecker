import logging, os
from logging.handlers import RotatingFileHandler

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_formatter = logging.Formatter('%(message)s')
file_handler = RotatingFileHandler('logs/datachecker.log', maxBytes=2000, backupCount=10)
file_handler.setFormatter(file_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def logInfo(text_to_display):
    logger.info('{}'.format(text_to_display))


def logError(text_to_display):
    logger.error('{}'.format(text_to_display))


def logWarn(text_to_display):
    logger.warning('{}'.format(text_to_display))
