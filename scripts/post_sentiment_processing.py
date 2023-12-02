import configparser
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from utilis.mongodb_helper import *
from utilis.settings import *
from utilis.mysql_helper import *

import mysql.connector
from mysql.connector import Error


path_to_settings = "/Users/liuminghuang/Repos/Reddit_Post_Pipeline/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)



def update_sql_db(connection, mysql_database, db_name, collection_name, date):
    '''
    update_sql_db: update redditTopic and Postsentiment table in MySQL
    '''
    list_mgdb_data= get_mongodb_data(subreddit_list, db_name, collection_name, date)
    if list_mgdb_data != []:
        for mgdb_data in list_mgdb_data:
            update_sql_db_single_subreddit(connection, mysql_database, mgdb_data)



def run_update_sql():
    '''
    run_update_sql: for airflow to run update_sql_db function
    '''
    mysql_connection = mysql.connector.connect(
            host=Configs['mysql_cred']['host'],       
            database= mysql_database,
            user=Configs['mysql_cred']['user'],     
            password=Configs['mysql_cred']['password'] 
        )
    update_sql_db(mysql_connection, mysql_database, mongodb_info['mgdb_db_name'], mongodb_info['mgdb_collection_name'], default_date)
        


def check_sql_connection():
    '''
    check_sql_connection: for airflow to check mysql connection
    '''
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
        print("Error while connecting to MySQL", e)



