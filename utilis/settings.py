import sys
import os
# Get the current working directory
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
sys.path.append(project_folder_path)

from datetime import datetime, timedelta
from utilis.reddit_helper import *



default_date = datetime.today().strftime('%Y-%m-%d')
mysql_database = "testing"
file_path = project_folder_path + '/utilis/subredditTopics.txt'
subreddit_list = get_subreddit_topics(file_path)
reddit_info = {
    'userAgentName': 'airflow',
    'numSubreddit': 40,
}
redis_info = {
    'rds_port': '6379',
    'rds_dbNum': 1,
    'rds_host': 'localhost',
    'rds_key': 'reddit_title_id'
}
mongodb_info = {
    'mgdb_db_name': 'chatgpt_reddit_thread',
    'mgdb_collection_name': 'top_posts'
}
