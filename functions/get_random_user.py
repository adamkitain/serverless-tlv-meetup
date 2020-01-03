from utils.mysql import GetMySQLClient
from random import randint
import logging
import json

db_client = GetMySQLClient()
logger = logging.getLogger()


def _get_random_user_id():
    user_ids = db_client.Query("select id from USERS limit 1000")
    user_id = user_ids[randint(0,999)]['id']
    logging.info("Found user: {}".format(user_id))
    return user_id


def _get_user_data(user_id):
    user_query = "select u.*, s.* from USERS u join SESSIONS s on u.id = s.user_id where u.id = '{}'".format(user_id)
    user_sessions = db_client.Query(user_query)
    logging.info("Found {} sessions".format(len(user_sessions)))
    return user_sessions


def _format_response(res_body):
    response = {
        "statusCode": 200,
        "body": json.dumps(res_body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    logger.info("Response: {}".format(response))
    return response


def handler(event, context):
    user_id = _get_random_user_id()
    user_data = _get_user_data(user_id)
    return _format_response(user_data)