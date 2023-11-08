import configparser
from pymongo import MongoClient
import os
from datetime import datetime
import time

path_to_settings = "/Users/liuminghuang/Repos/Reddit_Post_Pipeline/secrets.ini"
# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

mongodb_cred = {'mongo_user_id' : Configs['mongodb_cred']['user_id'],
'mongo_password' :  Configs['mongodb_cred']['password'],
'mongo_cluster_name': 'momo78932'}


# result = collection.insert_one(
#         {
#             'subreddit': 'chatgpt',
#             "date": "2023-11-07",
#             "submission": {"title": "selftext"}
#         }
# )
# result.inserted_id

class mongodb_connection:
    def __init__(self, mongodb_cred, db_name, collection_name):
        mongo_user_id = mongodb_cred['mongo_user_id']
        mongo_password = mongodb_cred['mongo_password']
        mongo_cluster_name = mongodb_cred['mongo_cluster_name']
        self.cluster  = MongoClient(f'mongodb+srv://{mongo_user_id}:{mongo_password}@{mongo_cluster_name}.ybq4rku.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.cluster[db_name]
        self.collection = self.db[collection_name]

        try:
            login_info = {"user": os.getlogin(),
                          "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          "status": "success"}
            self.test_collection = self.db['login_info']
            self.test_collection.insert_one(login_info)
        except Exception as e:
            raise(f"Error connecting to Mongodb: {e}")
        
        # get elements

        # drop elements

        # add one element

        # add many elements
        
if __name__ == "__main__":
    mongodb_connection(mongodb_cred, 'aggregation_example', 'nothing')

    