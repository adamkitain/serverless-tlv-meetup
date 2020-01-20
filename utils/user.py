import names
from random import randint
from utils.sls_logger import get_logger

logger = get_logger()


def get_random_user_id(db_client):
    random_first_names = ["'" + names.get_first_name() + "'" for i in range(10)]
    user_ids = db_client.Query("select id from USERS where first_name in ({})".format(",".join(random_first_names)))
    user_id = user_ids[randint(0,len(user_ids)-1)]['id']
    logger.info("Found user: {}".format(user_id))
    return user_id


def get_user_data(db_client, user_id):
    user_query = "select u.*, s.* from USERS u join SESSIONS s on u.id = s.user_id where u.id = '{}'".format(user_id)
    user_sessions = db_client.Query(user_query)
    logger.info("Found {} sessions".format(len(user_sessions)))
    return user_sessions

