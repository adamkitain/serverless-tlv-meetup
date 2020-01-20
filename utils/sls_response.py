import json
from utils.sls_logger import get_logger

logger = get_logger()


def format_success_response(res_body):
    response = {
        "statusCode": 200,
        "body": json.dumps(res_body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    logger.info("Response: {}".format(response))
    return response
