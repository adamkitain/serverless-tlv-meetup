import time
from random import randint
from utils.sls_logger import get_logger
from utils.mysql import GetMySQLClient
from utils.sls_response import format_success_response
from utils.user import get_random_user_id


logger = get_logger()
logger.info("----- COLD START ------")
db_client = GetMySQLClient()


def handle(event, context):
    time.sleep(randint(30,50)/10)
    user_id = get_random_user_id(db_client)
    time.sleep(randint(30,50)/10)
    return format_success_response({'user_id': user_id})