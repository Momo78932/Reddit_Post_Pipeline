import sys
import os
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
sys.path.append(project_folder_path)
import mysql.connector
from mysql.connector import Error
import configparser
from scripts.SQL.interact_with_sql_db_query import *
from textblob import TextBlob
from datetime import date
from datetime import datetime, timedelta
import csv



# read configuration from settings
path_to_settings = project_folder_path +"/secrets.ini"
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

def update_RedditTopic_table(connection, mysql_database, mgdb_data_subthread):
    '''
    update RedditTopic Table if 
    update_RedditTopic_table_query: sql_connection -> None
    '''
    mycursor = connection.cursor()
    update_RedditTopic_table_query = check_insert_query.format(mysql_database,mgdb_data_subthread, mysql_database, mgdb_data_subthread)
    mycursor.execute(update_RedditTopic_table_query)
    connection.commit()

def fetch_subreddit_id(connection, mysql_database,mgdb_data_subthread):
    '''
    fetching id of corresponding subreddit_name
    '''
    mycursor = connection.cursor()
    fetching_id_query = get_id.format(mysql_database, mgdb_data_subthread)
    mycursor.execute(fetching_id_query)
    result = mycursor.fetchall()
    return result

def get_reddit_post_id(connection, mysql_database, post_id):
    '''
    get post id from PostSentiment
    '''
    mycursor = connection.cursor()
    get_post_id_query = get_post_id.format(mysql_database, post_id)
    mycursor.execute(get_post_id_query)
    isin_id = mycursor.fetchall()
    return isin_id

def get_news_id(connection, mysql_database, news_id):
    '''
    get news id from NewsSentiment
    '''
    mycursor = connection.cursor()
    get_news_id_query = get_news_id.format(mysql_database, news_id)
    mycursor.execute(get_news_id_query)
    isin_id = mycursor.fetchall()
    return isin_id

def insert_post_PostSentiment(connection, mysql_database, post_id, subreddit_id, DateGenerated, DateInserted, title, subjectivity, polarity):
    '''
    insert post data into PostSentiment
    '''
    mycursor = connection.cursor()
    insert_post_data_query = insert_post_data.format(mysql_database, post_id, subreddit_id, DateGenerated, DateInserted,title, subjectivity, polarity)
    mycursor.execute(insert_post_data_query)
    connection.commit()

def insert_news_NewsSentiment(connection, mysql_database, news_id, subreddit_id, date_generated, date_inserted, polarity):
    '''
    insert news data into NewsSentiment
    '''
    mycursor = connection.cursor()
    
    insert_news_query = insert_news_data.format(mysql_database)
    data = (news_id, subreddit_id, date_generated, date_inserted, polarity)
    mycursor.execute(insert_news_query, data)
    connection.commit()


def output_csv_posts(connection, mysql_database, folder_path, file_name):
    '''
    output_csv_posts: output csv posts data to designated path
    '''
    cursor = connection.cursor()
    load_post_query = load_post.format(mysql_database)
    cursor.execute(load_post_query)
    rows = cursor.fetchall()
    column_headers = [i[0] for i in cursor.description]
    csv_filename =  os.path.join(folder_path, file_name)
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(column_headers)
        csv_writer.writerows(rows)
    cursor.close()
    


def output_csv_news(connection, mysql_database, folder_path, file_name):
    '''
    output_csv_news: output csv news data to designated path
    '''
    cursor = connection.cursor()
    load_post_query = load_news.format(mysql_database)
    cursor.execute(load_post_query)
    rows = cursor.fetchall()
    column_headers = [i[0] for i in cursor.description]
    csv_filename =os.path.join(folder_path, file_name) 
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(column_headers)
        csv_writer.writerows(rows)
    cursor.close()
    connection.close()

    

def update_sql_db_single_subreddit_posts(mysql_connection, mysql_database, mgdb_data):
    '''
    update_sql_db_single_subreddit_posts:
     Effect: update redditTopic and Postsentiment table in MySQL
    update_sql_db_single_subreddit_posts: sql.connection Str Str -> None
    
    '''
    # update RedditTopic table
    update_RedditTopic_table(mysql_connection, mysql_database,mgdb_data['subthread'])
    
    # fetching id of corresponding subreddit_name
    result = fetch_subreddit_id(mysql_connection, mysql_database,mgdb_data['subthread'])
    
    if result != []:
        order = 1
        subreddit_id = result[0][0]
        mobgodb_default_id = str(mgdb_data['_id'])
        DateGenerated = mgdb_data['Date']
        for _ in mgdb_data['submissions']:
            post_id = mobgodb_default_id + str(order)
            isin_id = get_reddit_post_id(mysql_connection, mysql_database, post_id)
            if isin_id == []:
                DateInserted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                title = mgdb_data['submissions'][order-1]['title']
                escaped_title = title.replace("'", "''")
                blob = TextBlob(title)
                polarity = round(blob.sentiment[0],3)
                subjectivity = round(blob.sentiment[1],3)
                insert_post_PostSentiment(mysql_connection, mysql_database, post_id, subreddit_id, DateGenerated, DateInserted, escaped_title,  subjectivity, polarity)
                order += 1

def update_sql_db_single_subreddit_news(mysql_connection, mysql_database, mgdb_data_news):
    '''
    update_sql_db_single_subreddit_news:
     Effect: update redditTopic and Postsentiment table in MySQL
    update_sql_db_single_subreddit_news: sql.connection Str Str -> None
    
    '''
    # fetching id of corresponding subreddit_name
    result = fetch_subreddit_id(mysql_connection, mysql_database, mgdb_data_news['topic'])
    
    if result != []:
        order = 1
        subreddit_id = result[0][0]
        mongodb_default_id = str(mgdb_data_news['_id'])
        DateGenerated = mgdb_data_news['date']
        for _ in mgdb_data_news['articles']:
            news_id = mongodb_default_id + str(order)
            isin_id = get_reddit_post_id(mysql_connection, mysql_database, news_id)
            if isin_id == []:
                DateInserted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                title = mgdb_data_news['articles'][order-1]['title']

                blob = TextBlob(title)
                polarity = round(blob.sentiment[0],3)

                insert_news_NewsSentiment(mysql_connection, mysql_database, news_id, 
                                        subreddit_id, DateGenerated, DateInserted, polarity)
                order += 1

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