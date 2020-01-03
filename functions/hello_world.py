import logging
logger = logging.getLogger()

def handle(event, context):
    logger.info(event)
    logger.info(context)
    return "Hello, world"