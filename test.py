import praw
import configparser
import redis
from pymongo import MongoClient
db = MongoClient('mongodb+srv://momo78932:2gc543wG3etmmXA0@momo78932.ybq4rku.mongodb.net/?retryWrites=true&w=majority').aggregation_example
result = db.nothing.insert_many(
        [
        {"x": 1, "tags": ["dog", "cat"]},
        {"x": 2, "tags": ["cat"]},
        {"x": 2, "tags": ["mouse", "cat", "dog"]},
        {"x": 3, "tags": []},
    ]
)

#result.inserted_ids

l = []
mycol = db['nothing']
for x in mycol.find():
    l.append(x)
print(l[0])







path_to_settings = "/Users/liuminghuang/Repos/Reddit_Post_Pipeline/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

client_id=Configs['reddit_cred']['client_id']
client_secret=Configs['reddit_cred']['client_secret']


# reddit = praw.Reddit(
#     client_id=client_id,
#     client_secret=client_secret,
#     user_agent="testing_reddit_thread",
# )
# for submission in reddit.subreddit("ChatGPT").hot(limit=10sgg):
#     print(submission.id)
#     print('****' * 2)

# r = redis.Redis(host='localhost', port=6379, decode_responses=True, db = 1)
# print([val for val in r.smembers('nset')])
# r.sadd('nset', 3)
# print([val for val in r.smembers('nset')])

