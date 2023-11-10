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


def get_thread(userAgentName, subredditName, numSubreddit):
    try:
        reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=userAgentName
        )
        r = redis_connection('6379', 1, 'localhost')
        mgdb_client = mongodb_connection(mongodb_cred, 'chatgpt_reddit_thread', 'top_posts')
        distinct_post_id = r.get_elements('distinct_reddit_post_id')
        submission_document = {'subthread': subredditName, 'Date': datetime.now().strftime('%Y-%m-%d')}
        submission_id_to_add = set()
        submissions = []
        for submission in reddit.subreddit(subredditName).hot(limit=numSubreddit):
            if submission.id not in distinct_post_id:
                submissions.append({'title': submission.title, 'body': submission.selftext})
                submission_id_to_add.add(submission.id)
        submission_document['submissions'] = submissions
        mgdb_client.add_document(submission_document)
        for id in submission_id_to_add:
            r.add_elements('reddit_title_id', id)
    except Exception as e:
        raise(f"Error accesing Reddit Thread {subredditName}: {e}")
    

if __name__ == "__main__":
    userAgentName = 'testing'
    subredditName = 'ChatGPT'
    numSubreddit = 10
    get_thread(userAgentName, subredditName, numSubreddit)
