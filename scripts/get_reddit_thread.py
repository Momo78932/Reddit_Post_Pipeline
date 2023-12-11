import praw
from prawcore import NotFound
import configparser
import sys
import os
# Get the current working directory
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]


sys.path.append(project_folder_path)
from utilis.redis_helper import *
from utilis.mongodb_helper import *
from utilis.reddit_helper import *
from utilis.settings import *
from utilis.news_helper import *
from datetime import datetime

path_to_settings = project_folder_path +"/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

client_id=Configs['reddit_cred']['client_id']
client_secret=Configs['reddit_cred']['client_secret']


def get_thread(rdt_subredditTopic, rdt_info, rds_info, mgdb_info):
    '''
    get_thread: load daily Reddit posts info to redis and Mongodb database
    '''
    try:
        reddit = praw.Reddit(
        client_id=Configs['reddit_cred']['client_id'],
        client_secret=Configs['reddit_cred']['client_secret'],
        user_agent=rdt_info['userAgentName']
        )
        r = redis_connection(rds_info['rds_port'], rds_info['rds_dbNum'], rds_info['rds_host'])
        mgdb_client = mongodb_connection(mongodb_cred, mgdb_info['mgdb_db_name'], mgdb_info['mgdb_collection_name_posts'])
        distinct_post_id = r.get_elements(rds_info['rds_key'])
        submission_document = {'subthread': rdt_subredditTopic, 'Date': datetime.now().strftime('%Y-%m-%d')}
        submission_id_to_add = set()
        submissions = []
        for submission in reddit.subreddit(rdt_subredditTopic).hot(limit=rdt_info['numSubreddit']):
            if submission.id not in distinct_post_id:
                submissions.append({'title': submission.title, 'body': submission.selftext})
                submission_id_to_add.add(submission.id)
        submission_document['submissions'] = submissions
        if len(submission_document['submissions']) != 0:
            mgdb_client.add_document(submission_document)
            for id in submission_id_to_add:
                r.add_elements(rds_info['rds_key'], id)
        else:
            print("No document to add")
    except Exception as e:
        raise(f"Error accesing Reddit Thread {rdt_subredditTopic}: {e}")
    

def get_news(date):
    """
    get news for user defined interest
    """
    api_key=Configs['news_api_cred']['api_key']
    mgdb_client = mongodb_connection(mongodb_cred, mongodb_info['mgdb_db_name'], mongodb_info['mgdb_collection_name_news'])
    for topic in topic_list:
        news_dict = get_news_single_topic(topic, date, api_key)
        if news_dict['totalResults'] != 0:
            news_dict['date'] = date
            news_dict['topic'] = topic
            mgdb_client.add_document(news_dict)



def run_get_news():
    '''
    run_get_news: for airflow to import today's news data
    '''
    get_news(default_date)



def run_get_thread():
    '''
    run_get_thread: for airflow to run get_thread function
    '''
    for st in topic_list:
        get_thread(st,reddit_info, redis_info, mongodb_info)


    
    
    


