from utils.sls_response import format_success_response
from utils.user import get_user_data, get_random_user_id
from utils.sls_logger import get_logger
from utils.mysql import GetMySQLClient

logger = get_logger()
logger.info("----- COLD START ------")
db_client = GetMySQLClient()

def handle(event, context):
    user_id = get_random_user_id(db_client)
    user_data = get_user_data(db_client, user_id)
    return format_success_response(user_data)


