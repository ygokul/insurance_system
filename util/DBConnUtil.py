import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(connection_string=None):
        try:
            if connection_string is None:
                connection_string = DBPropertyUtil.get_connection_string("db_properties.ini")
            
            # Parse connection string
            params = dict(pair.split('=') for pair in connection_string.split())
            
            connection = mysql.connector.connect(
                host=params['host'],
                database=params['dbname'],
                user=params['user'],
                password=params['password'],
                port=int(params.get('port', '3306'))
            )
            
            print("Connection established successfully")
            return connection
        except Exception as e:
            print(f"Error establishing database connection: {e}")
            raise