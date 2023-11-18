import praw
import configparser
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from utilis.redis_helper import redis_connection
from utilis.mongodb_helper import mongodb_connection, mongodb_cred
from datetime import datetime

path_to_settings = "/Users/liuminghuang/Repos/Reddit_Post_Pipeline/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

client_id=Configs['reddit_cred']['client_id']
client_secret=Configs['reddit_cred']['client_secret']


def get_thread(userAgentName, subredditName, numSubreddit, rds_port, rds_dbNum, rds_host, rds_key, mgdb_db_name, mgdb_collection_name):
    try:
        reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=userAgentName
        )
        r = redis_connection(rds_port, rds_dbNum, rds_host)
        mgdb_client = mongodb_connection(mongodb_cred, mgdb_db_name, mgdb_collection_name)
        distinct_post_id = r.get_elements(rds_key)
        submission_document = {'subthread': subredditName, 'Date': datetime.now().strftime('%Y-%m-%d')}
        submission_id_to_add = set()
        submissions = []
        for submission in reddit.subreddit(subredditName).hot(limit=numSubreddit):
            if submission.id not in distinct_post_id:
                submissions.append({'title': submission.title, 'body': submission.selftext})
                submission_id_to_add.add(submission.id)
        submission_document['submissions'] = submissions
        # print(len(submission_document['submissions']))
        if len(submission_document['submissions']) != 0:
            mgdb_client.add_document(submission_document)
            for id in submission_id_to_add:
                r.add_elements(rds_key, id)
        else:
            print("No document to add")
    except Exception as e:
        raise(f"Error accesing Reddit Thread {subredditName}: {e}")
    


def run_get_thread():
    rdt_userAgentName = 'airflow'
    rdt_subredditName = 'ChatGPT'
    rdt_numSubreddit = 10

    rds_port = '6379'
    rds_dbNum = 1
    rds_host = 'localhost'
    rds_key = 'reddit_title_id'

    mgdb_db_name = 'chatgpt_reddit_thread'
    mgdb_collection_name = 'top_posts'


    get_thread(rdt_userAgentName, rdt_subredditName, rdt_numSubreddit, rds_port, rds_dbNum, rds_host, rds_key, mgdb_db_name, mgdb_collection_name)




if __name__ == "__main__":
    userAgentName = 'testing'
    subredditName = 'ChatGPT'
    numSubreddit = 10

    rds_port = '6379'
    rds_dbNum = 1
    rds_host = 'localhost'
    rds_key = 'nset'

    mgdb_db_name = 'chatgpt_reddit_thread'
    mgdb_collection_name = 'top_posts'


    get_thread(userAgentName, subredditName, numSubreddit, rds_port, rds_dbNum, rds_host, rds_key, mgdb_db_name, mgdb_collection_name)


