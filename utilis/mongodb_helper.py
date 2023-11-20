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
                'mongo_cluster_name': 'momo78932'
                }


class mongodb_connection:
    def __init__(self, mongodb_cred, db_name, collection_name):
        user_id = mongodb_cred['mongo_user_id']
        password = mongodb_cred['mongo_password']
        cluster_name = mongodb_cred['mongo_cluster_name']
        self.cluster  = MongoClient(f'mongodb+srv://{user_id}:{password}@{cluster_name}.ybq4rku.mongodb.net/?retryWrites=true&w=majority')
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
        
    # get documents
    def get_documents(self, prompt = None):
        '''
        get_documents: dictionary -> (list)
        '''
        db_items = []
        for item in self.collection.find(prompt):
            db_items.append(item)
        return db_items
        
    # drop document(s)
    def drop_document(self, prompt, drop_one=True):
        # notify user the results
        if self.collection.count_documents(prompt, limit = 1) == 0:
            print(f'Document: {prompt} doesn\'t exist')
        elif drop_one:
            self.collection.delete_one(prompt)
            print(f'Document: {prompt} successfully deleted')
        else:
            res = self.collection.delete_many(prompt)
            print(f'{res.deleted_count} documents matching pattern {prompt} successfully deleted')

    

    # add many documents
    def add_document(self, item):
        '''
        item can be list of items or single item
        add_document: (listof doc, bool) -> None
        Effect: add list of documents to self
        '''
        if type(item) == list:
            self.collection.insert_many(item)
            print(f'{len(item)} documents successfully added')
        elif type(item) == dict:
            self.collection.insert_one(item)
            print(f'Documents successfully added')
        else:
            print('Failed. Provide valid type of document')


def check_mongodb_connection():
    mongodb_connection(mongodb_cred, 'aggregation_example', 'things')





        


    