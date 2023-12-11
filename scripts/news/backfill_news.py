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
from utilis.settings import *
from datetime import datetime
from scripts.get_reddit_thread import *

# Set the start date and end date
start_date_str = '2023-11-09'
end_date = datetime.now() - timedelta(days=1) 
start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

# Generate a list of dates from the start date to one day before today (yesterday)
date_list = [(start_date + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, (end_date - start_date).days + 1)]

path_to_settings = project_folder_path +"/secrets.ini"

# read configuration from settings
Configs = configparser.ConfigParser()
Configs.read(path_to_settings)

client_id=Configs['reddit_cred']['client_id']
client_secret=Configs['reddit_cred']['client_secret']

for d in date_list:
    get_news(d)

