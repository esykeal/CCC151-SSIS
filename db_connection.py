import mysql.connector
import config

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database=config.database_name
    )