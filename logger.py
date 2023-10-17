import logging
import logging.handlers
from logging.handlers import QueueHandler
from logging.handlers import QueueListener

LOG_FILENAME = 'cninfo.log'
logger = logging.getLogger()


def create_queue_listener(queue):
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    file_handler.setFormatter(formatter)
    queue_listener = QueueListener(queue, file_handler)
    return queue_listener

def set_logger(queue=None):
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    if queue:
        queue_handler = QueueHandler(queue)
        queue_handler.setFormatter(formatter)
        logger.addHandler(queue_handler)
    else:
        file_handler = logging.handlers.RotatingFileHandler(
            LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


set_logger()
