import praw
import configparser

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
        for submission in reddit.subreddit(subredditName).hot(limit=numSubreddit):
            print(submission.selftext)
    except Exception as e:
        raise(f"Error accesing Reddit Thread {subredditName}: {e}")


if __name__ == "__main__":
    userAgentName = 'testing'
    subredditName = 'ChatGPT'
    numSubreddit = 10
    get_thread(userAgentName, subredditName, numSubreddit)