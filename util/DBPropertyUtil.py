import configparser
import os

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file_name):
        try:
            config = configparser.ConfigParser()
            config.read(property_file_name)
            
            if not config.has_section('db'):
                raise Exception("Database configuration section not found in the property file.")
                
            host = config.get('db', 'host')
            database = config.get('db', 'database')
            user = config.get('db', 'user')
            password = config.get('db', 'password')
            port = config.get('db', 'port', fallback='3306')
            
            return f"host={host} dbname={database} user={user} password={password} port={port}"
        except Exception as e:
            print(f"Error reading property file: {e}")
            raise