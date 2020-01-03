import MySQLdb
import logging
logger = logging.getLogger()

class DatabaseClient(object):

    def __init__(self, db_host, db_name, db_user, db_pass, db_port):
        self.db_host = db_host
        self.db_name = db_name
        self.connection = self.GetConnection(db_host, db_name, db_user, db_pass, db_port)
        self.cursor = self._GetCursor()

    def GetConnection(self, db_host, db_name, db_user, db_pass, db_port):
        raise NotImplementedError

    def Execute(self, query):
        """
        Execute a query and then commit to the database
        """
        try:
            self.cursor.execute(query)
        except Exception as e:
            self.connection.rollback()
            logger.info("There was an error on the query: {}".format(query))
            logger.error(e.message)
        finally:
            self.connection.commit()

    def Query(self, query, as_dict=True):
        """
        Query the DB and collect the results. Special handling for one-field queries.
        Returns None on error
        """
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            colnames = [desc[0].lower() for desc in self.cursor.description] if as_dict else None
            if len(results) == 0:
                return []
            return self._FormatResults(results, colnames)
        except Exception, e:
            self.connection.rollback()
            logger.info("There was an error on the query: {}".format(query))
            logger.error(e.message)
            return None

    @staticmethod
    def _FormatResults(results, columns):
        if not columns:
            if len(results[0]) == 1:
                results = [row[0] for row in results]
            return results
        if len(columns) != len(results[0]):
            logger.warn(
                "Column labels ({}) and results ({}) are not the same length".format(len(columns), len(results[0])))
        return [dict(zip(columns, row)) for row in results]

    def _GetCursor(self):
        return self.connection.cursor()

class MysqlClient(DatabaseClient):

    def __init__(self, db_host, db_name, db_user, db_pass, db_port=3306):
        """
        Create a MySQLClient Object and connect to the DB
        """
        super(MysqlClient, self).__init__(db_host, db_name, db_user, db_pass, db_port)

    def GetConnection(self, db_host, db_name, db_user, db_pass, db_port):
        return MySQLdb.connect(host=db_host,
                               port=db_port,
                               db=db_name,
                               user=db_user,
                               passwd=db_pass, charset='utf8')

    def _GetCursor(self):
        return self.connection.cursor()

