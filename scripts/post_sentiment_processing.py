import configparser
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from utilis.mongodb_helper import mongodb_connection, mongodb_cred
from utilis.settings import *
from scripts.SQL.interact_with_sql_db_query import *

import mysql.connector
from mysql.connector import Error

from datetime import date

path_to_settings = "/Users/liuminghuang/Repos/Reddit_Post_Pipeline/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

def get_mongodb_data(subredditName, db_name, collection_name):
    '''
    get_mongodb_data: get today's post data from Mongodb 
    '''
    client = mongodb_connection(mongodb_cred, db_name, collection_name)
    prompt = {'subthread':subredditName,'Date':date.today().strftime("%Y-%m-%d")}
    return client.get_documents(prompt)


# l = get_mongodb_data(reddit_info['subredditName'],mongodb_info['mgdb_db_name'], mongodb_info['mgdb_collection_name'])
# print(l[0].keys())
# print(type(l[0]['_id'])) # <class 'bson.objectid.ObjectId'>
# print(type(l[0]['subthread'])) # str
# print(type(l[0]['Date'])) # str
# print(type(l[0]['submissions'])) # list


def update_sql_db():
    '''
    update_sql_db: update redditTopic and Postsentiment table in MySQL
    '''
    connection = mysql.connector.connect(
        host=Configs['mysql_cred']['host'],       
        database='reddit_thread_analysis',
        user=Configs['mysql_cred']['user'],     
        password=Configs['mysql_cred']['password'] 
    )
    today_data= get_mongodb_data(reddit_info['subredditName'],mongodb_info['mgdb_db_name'], mongodb_info['mgdb_collection_name'])[0]
    # Check if the connection was successful
    if connection.is_connected():
        mycursor = connection.cursor()

        # update RedditTopic table
        update_RedditTopic_table_query = check_insert_query.format(today_data['subthread'],today_data['subthread'])
        # print(sql)
        mycursor.execute(update_RedditTopic_table_query)
        connection.commit()

        # fetching id of corresponding subreddit_name
        fetching_id_query = get_id.format(today_data['subthread'])
        mycursor.execute(fetching_id_query)
        result = mycursor.fetchall()
        if result != []:
            print(result)


update_sql_db()


# try: 
#     # Establish a database connection
#     connection = mysql.connector.connect(
#         host=Configs['mysql_cred']['host'],       
#         database='reddit_thread_analysis',
#         user=Configs['mysql_cred']['user'],     
#         password=Configs['mysql_cred']['password'] 
#     )
#     # Check if the connection was successful
#     if connection.is_connected():
#         db_info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_info)
#         cursor = connection.cursor()
        
#         # Execute a query
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

#         # Always close the connection and cursor
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

# except Error as e:
#     print("Error connecting to MySQL", e)