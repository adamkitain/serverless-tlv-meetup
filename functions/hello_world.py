import logging
import json

logger = logging.getLogger()


def handle(event, context):
    logger.info(event)
    logger.info(context)
    response = {
        "statusCode": 200,
        "body": json.dumps({"data": 3}),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response

