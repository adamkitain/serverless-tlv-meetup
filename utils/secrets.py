from botocore.exceptions import ClientError

from utils.sls_logger import get_logger
import boto3

logger = get_logger()

def get_secret(secret_key):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')

    try:
        logger.info("Retrieving secret {}".format(secret_key))
        get_secret_value_response = client.get_secret_value(SecretId=secret_key)
        return eval(get_secret_value_response['SecretString'])

    except ClientError as e:
        logger.info("Could not get secret key")
        logger.info(e.response)