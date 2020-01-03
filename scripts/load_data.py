from utils.mysql import MysqlClient
import uuid
import names
import random
FIRST_NAMES = [names.get_first_name() for i in range(1000)]
LAST_NAMES = [names.get_last_name() for i in range(1000)]

USERS_SIZE=250000
SESSIONS_SIZE=10

def _parse_options():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--db_host')
    parser.add_option('--db_user')
    parser.add_option('--db_pass')
    options, args = parser.parse_args()
    return options

def _create_table(db_client):
    drop_query = "DROP TABLE IF EXISTS USERS;"
    db_client.Execute(drop_query)

    create_query = """CREATE TABLE USERS (
        ID              VARCHAR(255),
        FIRST_NAME      VARCHAR(255),
        LAST_NAME       VARCHAR(255),
        HIGH_SCORE      INTEGER
        );
    """
    db_client.Execute(create_query)

    drop_query = "DROP TABLE IF EXISTS SESSIONS;"
    db_client.Execute(drop_query)

    create_query = """CREATE TABLE SESSIONS (
        USER_ID         VARCHAR(255),
        TIMESTAMP       INTEGER,
        SCORE           INTEGER
        );
    """
    db_client.Execute(create_query)


def _create_fake_record():
    return (str(uuid.uuid4()), FIRST_NAMES[random.randint(0,999)], LAST_NAMES[random.randint(0,999)], random.randint(0, 10000))


def _insert_fake_users_data_to_db(db_client, fake_data):
    fake_data_str = ',\n'.join([str(r) for r in fake_data])
    insert_str = """INSERT INTO USERS VALUES {};""".format(fake_data_str)
    db_client.Execute(insert_str)


def _insert_fake_sessions_data_to_db(db_client):
    for i in range(SESSIONS_SIZE):
        timestamp = random.randint(1577000000, 1578000000)
        insert_sessions_str = """INSERT INTO SESSIONS (SELECT ID AS USER_ID, 
                                                              {} AS TIMESTAMP, 
                                                              {} AS SCORE FROM USERS);""".format(timestamp, 100)
        db_client.Execute(insert_sessions_str)


def _load_fake_data(db_client, total_rows=1000, batch_size=1000):
    for i in range(int(total_rows/batch_size)):
        fake_data = list()
        for j in range(batch_size):
            fake_data.append(_create_fake_record())

        _insert_fake_users_data_to_db(db_client, fake_data)
    _insert_fake_sessions_data_to_db(db_client)


def create_tables_load_data(db_host, db_user, db_pass):
    db_client = MysqlClient(db_host, 'sls_demo', db_user, db_pass)
    _create_table(db_client)
    _load_fake_data(db_client, total_rows=USERS_SIZE, batch_size=1000)

if __name__ == '__main__':
    options = _parse_options()
    create_tables_load_data(options.db_host, options.db_user, options.db_pass)
