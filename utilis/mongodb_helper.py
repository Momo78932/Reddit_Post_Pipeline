import configparser
from pymongo import MongoClient
from datetime import datetime
import os

current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
path_to_settings = project_folder_path + "/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

mongodb_cred = {'mongo_user_id' : Configs['mongodb_cred']['user_id'],
                'mongo_password' :  Configs['mongodb_cred']['password'],
                'mongo_cluster_name': Configs['mongodb_cred']['cluster_name']
                }


class mongodb_connection:
    def __init__(self, mongodb_credential, db_name, collection_name):
        user_id = mongodb_credential['mongo_user_id']
        password = mongodb_credential['mongo_password']
        cluster_name = mongodb_credential['mongo_cluster_name']
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
        get_documents(self, prompt = None): return a list of documentation from mongodb client that matches prompt pattern, if prompt is None, return all documentations
        get_documents: Any -> (listof Dict)
        '''
        db_items = []
        for item in self.collection.find(prompt):
            db_items.append(item)
        return db_items
        
    # drop document(s)
    def drop_document(self, prompt, drop_one=True):
        '''
        drop_document(self, prompt, drop_one=True): drop documentations that matches prompt pattern
        drop_document: dict bool -> None
        '''
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
        add_document(self, item): item can be list of items or single item
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

def get_mongodb_data_posts(subredditlist, db_name, collection_name, date):
    '''
    get_mongodb_data_posts(subredditlist, db_name, collection_name, date): get today's post data from Mongodb - 1 dictionary for 1 subreddit
    get_mongodb_data_posts: (listof Str) Str Str Str -> (listof Dict)
    '''
    doc_list = []
    for subredditName in subredditlist:
        single_dict = get_mongodb_data_single_posts(subredditName, db_name, collection_name, date)
        if single_dict != {}:
            doc_list.append(single_dict)  
    return doc_list


def get_mongodb_data_single_posts(subredditName, db_name, collection_name, date):
    '''
    get_mongodb_data_single: gether post data for date and subredditName in one dictionary
    get_mongodb_data_single: Str Str Str Str -> Dict
    '''
    client = mongodb_connection(mongodb_cred, db_name, collection_name)
    prompt = {'subthread':subredditName,'Date':date}
    l_doc = client.get_documents(prompt)

    if l_doc != []:
        final_doc = l_doc[0]
        l_submissions = list(map(lambda d: d['submissions'], l_doc))
        final_submission = []
        for entry in l_submissions:
            final_submission.extend(entry)
        final_doc['submissions'] = final_submission
        return final_doc
    else:
        return {}


def get_mongodb_data_news(subredditlist, db_name, collection_name, date):
    '''
    get_mongodb_data_news(subredditlist, db_name, collection_name, date): get today's post data from Mongodb - 1 dictionary for 1 subreddit
    get_mongodb_data_news: (listof Str) Str Str Str -> (listof Dict)
    '''
    doc_list = []
    for topic in subredditlist:
        single_dict = get_mongodb_data_single_news(topic, db_name, collection_name, date)
        if single_dict != {}:
            doc_list.append(single_dict)  
    return doc_list
    

def get_mongodb_data_single_news(subredditName, db_name, collection_name, date):
    '''
    get_mongodb_data_single_news: gether post data for date and subredditName in one dictionary
    get_mongodb_data_single_news: Str Str Str Str -> Dict
    '''
    client = mongodb_connection(mongodb_cred, db_name, collection_name)
    prompt = {'topic':subredditName ,'date':date}
    l_doc = client.get_documents(prompt)

    if l_doc != []:
        final_doc = l_doc[0]
        l_articles = list(map(lambda d: d['articles'], l_doc))

        final_article = []
        for entry in l_articles:
            final_article.extend(entry)
        # turn source into source_id and source_name
        for item in final_article:
            if 'source' in item:
                item['source_id'] = item['source']['id']
                item['source_name'] = item['source']['name']
                del item['source'] 
            if 'url' in item:
                del item['url'] 
            if 'content' in item:
                del item['content'] 
        final_doc['articles'] = final_article
        return final_doc
    else:
        return {}
    



def check_mongodb_connection():
    '''
    check_mongodb_connection(): for airflow to run to check mongodb connection
    '''
    mongodb_connection(mongodb_cred, 'aggregation_example', 'things')





        


    