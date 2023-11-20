import configparser
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from utilis.mongodb_helper import mongodb_connection, mongodb_cred

import mysql.connector
from mysql.connector import Error

path_to_settings = "/Users/liuminghuang/Repos/Reddit_Post_Pipeline/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)


try: 
    # Establish a database connection
    connection = mysql.connector.connect(
        host=Configs['mysql_cred']['host'],       
        database='reddit_thread_analysis',
        user=Configs['mysql_cred']['user'],     
        password=Configs['mysql_cred']['password'] 
    )
    # Check if the connection was successful
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        
        # Execute a query
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        # Always close the connection and cursor
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

except Error as e:
    print("Error connecting to MySQL", e)