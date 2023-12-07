import requests
import configparser
import sys
import os
# Get the current working directory
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
sys.path.append(project_folder_path)
from utilis.settings import *

# read configuration from settings
path_to_settings = project_folder_path +"/secrets.ini"
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

api_key=Configs['news_api_cred']['api_key']

def get_news(mgdb_client, date):
    """
    get news for user defined interest
    """
    for topic in topic_list:
        news_dict = get_news_single_topic(topic, date, api_key)
        if news_dict['totalResults'] != 0:
            news_dict['date'] = date
            mgdb_client.add_document(news_dict)

def get_news_single_topic(topic, date, api_key):
    base_url = "https://newsapi.org/v2/everything?"
    query_params = {
        'q': topic, 
        'from': date,  
        'apiKey': api_key,
        'language': 'en',  
    }
    response = requests.get(base_url, params=query_params)
    news_data = response.json()
    return news_data
