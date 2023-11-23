------ RedditPost Project ------

RedditPost project builds a data pipeline for users to analyze sentiment for a specific reddit thread.
Built with technologies such as Redis, MongoDB and ...
It provides a seamless experience for personal and professional use.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Log](#log)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## Installation
To install RedditPost project, you'll need Redis and Mysql installed on your computer
Python version: 3.10.10

## Log
11.1
- set up virtual environment: reddit_venv
- set up new repository on Github
- sign up new Reddit account and request API
  
11.5
- install praw package to virtual environment
- add new folder: scripts
- add get_reddit_thread.py file to grab text from top posts in folder scripts
- add new folder: utilis - helper functions
- add redis_helper.py file to make change in local redis database
- edit test.py
- adit readme.md

11.7
- add duplicate check feature to function get_thread in file get_reddit_thread.py
- add __init__.py to folder utilis
- sign up and create account in Mongodb.atlas
- create new cluster in Mongodb: momo78932
- add new file: mongodb_helper.py to make change in Mongodb database in folder utilis
- edit test.py
- update read.md

11.9
- add functions: get_documents, drop_document, and add_document to file: mongodb_helper.py
- update get_reddit_thread to pull and store submission id to Redis and posts info to Mongodb
- run get_thread function for 11.9 top posts

11.10 
- run get_thread function for 11.10 top posts

11.11
- run get_thread function for 11.11 top posts

11.12
- run get_thread function for 11.12 top posts

11.13
- add new folder: dags
- add new file: load_reddit_thread.py
- add new function to mongodb_helper.py
- add new function to redit_helper.py
- found bug: duplicate item in Mongodb
- update get_thread function in get_reddit_thread.py

11.19
- add new folder: SQL in scripts 
- add new file create_table.sql to folder SQL
	- include sql script to add tables: RedditTopic and PostSentiment to MySQL
- add new file mysql_table.md to folder SQL
	- include description of the two tables: RedditTopic and PostSentiment

11.20 
- update .gitignore file to hide __pycache__, dump.rdb, and test.py
- move unit testing codes to test.py
- update get_thread function 
turn function arguments into dictionaries
