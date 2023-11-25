import configparser
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from utilis.mongodb_helper import mongodb_connection, mongodb_cred
from utilis.settings import *
from scripts.SQL.interact_with_sql_db_query import *

import mysql.connector
from mysql.connector import Error

from datetime import date
from datetime import datetime, timedelta

path_to_settings = "/Users/liuminghuang/Repos/Reddit_Post_Pipeline/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

def get_mongodb_data(subredditName, db_name, collection_name, date):
    '''
    get_mongodb_data: get today's post data from Mongodb 
    '''
    client = mongodb_connection(mongodb_cred, db_name, collection_name)
    prompt = {'subthread':subredditName,'Date':date}
    return client.get_documents(prompt)


def update_sql_db(date):
    '''
    update_sql_db: update redditTopic and Postsentiment table in MySQL
    '''
    connection = mysql.connector.connect(
        host=Configs['mysql_cred']['host'],       
        database='reddit_thread_analysis',
        user=Configs['mysql_cred']['user'],     
        password=Configs['mysql_cred']['password'] 
    )
    mgdb_data= get_mongodb_data(reddit_info['subredditName'],mongodb_info['mgdb_db_name'], mongodb_info['mgdb_collection_name'], date)
    if mgdb_data != []:
        mgdb_data = mgdb_data[0]
        # Check if the connection was successful
        if connection.is_connected():
            mycursor = connection.cursor()

            # update RedditTopic table
            update_RedditTopic_table_query = check_insert_query.format(mgdb_data['subthread'],mgdb_data['subthread'])
            mycursor.execute(update_RedditTopic_table_query)
            connection.commit()

            # fetching id of corresponding subreddit_name
            fetching_id_query = get_id.format(mgdb_data['subthread'])
            mycursor.execute(fetching_id_query)
            result = mycursor.fetchall()
            if result != []:
                order = 1
                subreddit_id = result[0][0]
                mobgodb_default_id = str(mgdb_data['_id'])
                DateGenerated = mgdb_data['Date']
                for reddit_post in mgdb_data['submissions']:
                    post_id = mobgodb_default_id + str(order)
                    # check if id exists in mysql database
                    get_post_id_query = get_post_id.format(post_id)
                    mycursor.execute(get_post_id_query)
                    isin_id = mycursor.fetchall()
                    if isin_id == []:
                        DateInserted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        title = mgdb_data['submissions'][order-1]['title']
                        variables = (post_id, subreddit_id, DateGenerated, DateInserted, title, post_id, subreddit_id, DateGenerated, DateInserted, title)
                        mycursor.execute(insert_post_data, variables)
                        connection.commit()
                        order += 1
        
def check_sql_connection():
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



def run_update_sql():
    update_sql_db(default_date)