# Developer Log

## Table of Contents

- [2023-11-01](#2023-11-01)
- [2023-11-05](#2023-11-05)
- [2023-11-07](#2023-11-07)
- [2023-11-09](#2023-11-09)
- [2023-11-13](#2023-11-13)
- [2023-11-19](#2023-11-19)
- [2023-11-20](#2023-11-20)
- [2023-11-22](#2023-11-22)
- [2023-11-26](#2023-11-26)
- [2023-11-29](#2023-11-29)
- [2023-12-01](#2023-12-01)
- [2023-12-03](#2023-12-03)

## 2023-11-01

### Added
- Initialized a new Python virtual environment `reddit_venv` for dependency management.
- Created a new GitHub repository for version control and collaboration.
- Registered a new Reddit account and applied for API access to support automated interactions with Reddit data.

## 2023-11-05

### Added
- Installed the `praw` package in the virtual environment to interface with the Reddit API.
- Created a `scripts` directory for storing Python scripts.
- Developed `get_reddit_thread.py` to extract top posts from Reddit; added to the `scripts` directory.
- Established a `utils` directory for utility and helper functions.
- Authored `redis_helper.py` to facilitate operations in a local Redis database.

### Changed
- Modified `test.py` to reflect new test cases for the `praw` interactions.
- Updated `readme.md` to provide setup instructions and project overview.

## 2023-11-07

### Added
- Enhanced `get_thread` function in `get_reddit_thread.py` to include duplicate checking logic.
- Introduced `__init__.py` in the `utils` directory to allow for package-like imports.
- Signed up for MongoDB Atlas, created a new cloud cluster `mongo78932`.
- Crafted `mongodb_helper.py` to manage interactions with the MongoDB database; stored in `utils`.

## 2023-11-09

### Added
- Added `get_documents`, `drop_document`, and `add_document` functions to `mongodb_helper.py` to enhance MongoDB interaction capabilities.

### Changed
- Updated `get_reddit_thread.py` to integrate functionality for storing submission IDs in Redis and post details in MongoDB.

## 2023-11-13

### Added
- Created a `dags` directory for storing directed acyclic graphs for workflow management.
- Composed `load_reddit_thread.py` script within `dags` for orchestrating data pipeline tasks.
- Augmented `mongodb_helper.py` and `reddit_helper.py` with additional utility functions.

### Changed
- Refined `get_thread` function in `get_reddit_thread.py` for better efficiency.

### Issues
- Identified and logged a bug causing duplicate entries in MongoDB.

## 2023-11-19

### Added
- Inaugurated a new `SQL` directory under `scripts` for SQL-related operations.
- Authored `create_table.sql` within the `SQL` directory to facilitate the creation of `RedditTopic` and `PostSentiment` tables in MySQL.
- Developed `mysql_table.md` providing a detailed description of the `RedditTopic` and `PostSentiment` tables.

## 2023-11-20

### Changed
- Updated `.gitignore` to exclude caching directories (`__pycache__`), Redis dump files (`dump.rdb`), and test scripts (`test.py`).

### Fixed
- Refactored `get_thread` function to accept arguments in dictionary format.
- Overhauled `get_thread` function for enhanced functionality.
- Relocated unit testing codes to `test.py` to streamline testing processes.

## 2023-11-22

### Added
- Added `post_sentiment_processing.py` script for processing sentiment analysis on Reddit posts.
- Implemented `get_mongodb_data` and `update_sql_db` functions within `post_sentiment_processing.py`.
- Introduced `interact_with_sql_db_query.py` to the project to manage SQL queries.
- Created `settings.py` to centralize application configuration settings.
- Composed `mysql_table.md` and `create_table.sql` for detailed MySQL table management.
- Established MySQL database `reddit_thread_analysis`.
- Constructed `RedditTopic` and `PostSentiment` tables within the MySQL database.


## 2023-11-26 

### Added
- Implemented a new Python script `load_mysql_data.py` in the `dags` directory for automated data loading to MySQL.
- Created a `requirements.txt` file to manage project dependencies more effectively.

### Changed
- Updated the `backfill_sql_db.py` script in `scripts/SQL` to enhance the data backfilling process.
- Refined the SQL table creation script `create_table.sql` in `scripts/SQL` to adjust the database schema.
- Enhanced `interact_with_sql_db_query.py` in `scripts/SQL` for improved database interaction and querying efficiency.
- Modified `post_sentiment_processing.py` in `scripts` to refine the sentiment analysis algorithm.
- Updated `settings.py` in `utils` to include new configuration settings.

### Notes
- The branch `11_26_function_review` indicates a focus on reviewing and refining functions.

## 2023-11-29

#### Added
- Introduced `reddit_helper.py` in the `utils` directory to encapsulate Reddit API interactions.
- Created `subredditTopics.txt` in the `utils` directory, allowing users to easily specify and modify the list of subreddit topics for data import.

#### Changed
- Updated `load_reddit_thread.py` in the `dags` directory with improved thread handling.
- Revised `get_reddit_thread.py` in the `scripts` directory to iterate over a list of valid subreddits defined by the user.
- Renamed `load_mysql_data.py` from `dags` to `utils` for better organization and consistency with other utility scripts.
- Modified `settings.py` in the `utils` directory to accommodate new configuration parameters.

#### Fixed
- Resolved the "Import Error" in Airflow by adjusting PYTHONPATH and ensuring proper imports.

#### Notes
- The changes made today were focused on enhancing the robustness of the data collection pipeline from Reddit and improving the manageability of the configurations. The renaming and reorganization of scripts reflect an ongoing effort to maintain a clean and logical structure in the codebase.

## 2023-12-01

#### Added
- Added `mysql_helper.py` in the `utils` directory to provide MySQL database interaction functions.

#### Changed
- Updated `backfill_sql_db.py` in the `scripts/SQL` directory with new optimizations.
- Enhanced `post_sentiment_processing.py` in the `scripts` directory for better accuracy in sentiment analysis.
- Refactored `mongodb_helper.py` in the `utils` directory to improve the interface and usability.

#### Fixed
- Fixed `post_sentiment_processing.py` to ensure compatibility with the new feature that allows pulling data from a dynamic list of subreddit topics defined in `subredditTopics.txt`.

#### Notes
- Today's updates focus on refining the data processing functions and extending the database interaction capabilities. The newly added `mysql_helper.py` enriches our suite of database tools, while changes to the sentiment analysis script align it with the latest feature set, enhancing its ability to process topic-specific data efficiently. These ongoing improvements underscore our commitment to building a robust and versatile analytics platform.


## 2023-12-03

#### Codebase Refinement
- Replaced hardcoded folder path in:
  - `get_reddit_thread.py`
  - `settings.py`
  - `mongodb_helper.py`
  - `load_reddit_thread.py`
  - `update_mysql_db.py`

#### Data Pipeline Updates
- Added DAG to update SQL database daily (`update_mysql_db.py`).

#### Identified Issues
- **Bug Fixed:**  
	- List out of range when running `backfill_sql_db.py`.
- **Bug Found:**
  - Import error with the two DAG files (`load_reddit_thread.py` and `update_mysql_db.py`).

#### Notes
- The focus was on identifying existing issues to set the stage for the next phase of bug fixes.
- Implemented a new DAG for automated daily updates to the SQL database, enhancing operational efficiency.
- Detected and logged new bugs, including an import error that affects DAG operations.
- Planned fixes and improvements will be addressed in the upcoming development cycle to ensure continuous integration and delivery.

