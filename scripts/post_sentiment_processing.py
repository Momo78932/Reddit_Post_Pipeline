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



def update_sql_db(connection, mysql_database, db_name, collection_name_posts, collection_name_news, date):
    '''
    update_sql_db: update redditTopic and Postsentiment table in MySQL
    '''
    list_mgdb_data_posts= get_mongodb_data_posts(topic_list, db_name, collection_name_posts, date)
    if list_mgdb_data_posts != []:
        for mgdb_data in list_mgdb_data_posts:
            update_sql_db_single_subreddit_posts(connection, mysql_database, mgdb_data)
    list_mgdb_data_news = get_mongodb_data_news(topic_list, db_name, collection_name_news, date)
    if list_mgdb_data_news != 0:
        for mgdb_data_news in list_mgdb_data_news:
            update_sql_db_single_subreddit_news(connection, mysql_database, mgdb_data_news)



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
    update_sql_db(mysql_connection, mysql_database, mongodb_info['mgdb_db_name'], mongodb_info['mgdb_collection_name_posts'], mongodb_info['mgdb_collection_name_news'], default_date)
    mysql_connection.close()




def update_csv_file():
    '''
    update_csv_file: for airflow to update output_post.csv and output_news.csv
    '''
    mysql_connection = mysql.connector.connect(
            host=Configs['mysql_cred']['host'],       
            database= mysql_database,
            user=Configs['mysql_cred']['user'],     
            password=Configs['mysql_cred']['password'] 
        )
    folder_path = os.path.join(project_folder_path, output_folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name_post = 'posts_output.csv'
    file_name_news = 'news_output.csv'
    output_csv_posts(mysql_connection, mysql_database, folder_path, file_name_post)
    output_csv_news(mysql_connection, mysql_database, folder_path, file_name_news)
    mysql_connection.close()







