import configparser
import sys
import os
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
sys.path.append(project_folder_path)

from utilis.mongodb_helper import *
from utilis.settings import *
from utilis.mysql_helper import *

import mysql.connector
from mysql.connector import Error


path_to_settings = project_folder_path+ "/secrets.ini"

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
        






