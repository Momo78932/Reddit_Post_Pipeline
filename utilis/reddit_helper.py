import praw
from prawcore import NotFound


def get_subreddit_topics(file_path):
    '''
    get_subreddit_topics(file_path): return a list of subreddit topics in file_path
    get_subreddit_topics: Str -> (listof Str)
    '''
    string_list = []
    with open(file_path, 'r') as file:
        for line in file:
            string_list.append(line.strip())
    return string_list
    

