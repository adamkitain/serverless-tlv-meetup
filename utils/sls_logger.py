import logging

logger = None


def get_logger():
    global logger
    if logger is not None:
        return logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    return logger
