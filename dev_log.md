
# Development Log

## Table of Contents
- [2023-11-01](#2023-11-01)
- [2023-11-05](#2023-11-05)
- [2023-11-07](#2023-11-07)
- [2023-11-09](#2023-11-09)
- [2023-11-13](#2023-11-13)
- [2023-11-19](#2023-11-19)
- [2023-11-20](#2023-11-20)
- [2023-11-22](#2023-11-22)

## 2023-11-01
#### Added
- Set up virtual environment: `reddit_venv`
- Set up new repository on GitHub
- Sign up new Reddit account and request API

## 2023-11-05
#### Added
- Install `praw` package to virtual environment
- Add new folder: `scripts`
- Add `get_reddit_thread.py` file to grab text from top posts in folder scripts
- Add new folder: `utils` - helper functions
- Add `redis_helper.py` file to make change in local Redis database

#### Changed
- Edit `test.py`
- Update `readme.md`

## 2023-11-07
#### Added
- Add duplicate check feature to function get_thread in file `get_reddit_thread.py`
- Add `__init__.py` to folder utils
- Sign up and create account in MongoDB atlas
- Create new cluster in MongoDB: `mongo78932`
- Add new file: `mongodb_helper.py` to make change in MongoDB database in folder utils

## 2023-11-09
#### Added
- Add functions: `get_documents`, `drop_document`, and `add_document` to file `mongodb_helper.py`

#### Changed
- Update `get_reddit_thread` to pull and store submission id to Redis and posts info to MongoDB

## 2023-11-13
#### Added
- Add new folder: `dags`
- Add new file: `load_reddit_thread.py`
- Add new function to `mongodb_helper.py`
- Add new function to `reddit_helper.py`

#### Changed
- Update `get_thread` function in `get_reddit_thread.py`

#### Issues
- Found bug: duplicate item in MongoDB

## 2023-11-19
#### Added
- Add new folder: `SQL` in scripts
- Add new file `create_table.sql` to folder `SQL`
  - Include SQL script to add tables: `RedditTopic` and `PostSentiment` to MySQL
- Add new file `mysql_table.md` to folder `SQL`
  - Include description of the two tables: `RedditTopic` and `PostSentiment`

## 2023-11-20
#### Changed
- Update `.gitignore` file to hide `__pycache__`, `dump.rdb`, and `test.py`

#### Fixed
- Turn function `get_thread` arguments into dictionaries
- Update `get_thread` function
- Move unit testing codes to `test.py`

## 2023-11-22
#### Added
- Add file: `post_sentiment_processing.py`
- Add function: `get_mongodb_data`
- Add function `update_sql_db`
- Add file: `interact_with_sql_db_query.py`
- Add file: `settings.py` file
- Add file: `mysql_table.md`
- Add file: `create_table.sql`
- Add MySQL database: `reddit_thread_analysis`
  - Add table: `RedditTopic`
  - Add table: `PostSentiment`