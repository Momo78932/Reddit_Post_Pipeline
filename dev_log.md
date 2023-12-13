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
- [2023-12-05](#2023-12-05)
- [2023-12-06](#2023-12-06)
- [2023-12-10](#2023-12-10)

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



## 2023-12-05

#### Codebase Updates
- Modified `create_table.sql` to add a "Title" column to the `PostSentiment` table in MySQL, enhancing data structure.
- Updated `interact_with_sql_db_query.py` and `mysql_helper.py` to accommodate the new column in data retrieval operations.
- Improved `post_sentiment_processing.py` for better accuracy in sentiment analysis and handling of special characters in INSERT statements.


#### Bugs and Fixes
- **Problem Found:**
  - Issue with the handling of special characters or string literals in INSERT statement.
- **Solution Implemented:**
  - Escaped single quotes within the title string to ensure proper SQL syntax.
  - Code Implementation: `escaped_title = title.replace("'", "''")`

#### Data Pipeline Enhancements
-  Add "Title" column to PostSentiment table in MySQL.
  - Problem: Handling of special characters or string literals in INSERT statement was causing errors.
  - Solution: Escaped single quotes in the title string to ensure proper SQL syntax. (`escaped_title = title.replace("'", "''")`)

#### Planned Improvements
- Export to CSV file and perform data analysis for in-depth insights.

#### Notes
- Today’s updates focused on refining data structures and improving data processing scripts.
- Addressed critical bugs affecting the data pipeline's reliability and efficiency.
- Preparing to conduct comprehensive data analysis with the newly updated and structured data.


## 2023-12-06

#### Data Analysis
- Converted sentiment polarity classifications into "neutral", "positive", and "negative".
- Visualized "title" data using a word cloud.
- Trained various ML models to evaluate sentiment analysis performance:
  - Multinomial Naïve Bayes
  - Logistic Regression
  - Random Forest
  - Support Vector Machines
- Analyzed the accuracy of each algorithm:
  - Multinomial Naive Bayes: 0.595420
  - Logistic Regression: 0.572519
  - Random Forest: 0.572519
  - Support Vector Machines: 0.564885
- Noted that news polarity might affect the result and planned to add a column for the day's average news polarity.

#### Codebase Refinement
- Implemented a new column for day's polarity in the data structure.
- Updated MongoDB scripts to include daily news updates and backfill operations.
- Created new files for news data processing:
  - `scripts/news/_init_.py`
  - `scripts/news/backfill_news.py`
  - `utils/news_helper.py`
- Modified `scripts/SQL/backfill_sql_db.py` for database improvements.
- Updated `scripts/get_reddit_thread.py` to fetch and process thread data more efficiently.
- Enhanced `post_sentiment_processing.py` for improved sentiment analysis.

#### To-do for Future
- [ ] Integrate the day's news polarity into MySQL database.
- [ ] Perform backfill operations for comprehensive data analysis.

#### Notes
- Focused on enhancing the accuracy of sentiment analysis by incorporating additional data and refining ML models.
- Prepared for future integration of news polarity into the data pipeline to enrich analysis.
- Scheduled backfill tasks to ensure completeness and integrity of historical data.

##  2023-12-10

#### Codebase Refinement
- Modified `update_sql_db` and `run_update_sql` function to load MongoDB news data to MySQL database.

#### Errors Found
- Encountered an error when running `backfill_sql_db.py`. Issue is currently under investigation.

#### Notes
- Today’s focus was on integrating MongoDB news data into the MySQL database to enrich our data set.
- Significant updates were made to the SQL scripts and utilities to improve data processing and management.
- An error was discovered in the `backfill_sql_db.py` script; troubleshooting is underway to resolve this as soon as possible.


##   2023-12-11

#### Updates and Improvements

- Implemented the `update_csv_file` function to enhance data maintenance for news and post datasets, improving the reliability of subsequent analysis.
- Added new visualizations in the "Data Visualization and Sentiment Analysis.ipynb" notebook:
  - Word cloud for better qualitative analysis of text data.
  - Joint Plot for visual correlation analysis between Reddit post subjectivity and polarity.
  - Point Plot to compare news polarity with Reddit post polarity, enabling a multi-dimensional view of sentiment trends.

#### Future To-dos

- Address data processing pipeline (DAG):
  - `run_get_thread()` to load today's post data.
  - `run_get_news()` to load today's news data.
  - `run_update_sql()` to integrate post and news data into the MySQL database.
  - `update_csv_file()` to export the MySQL database to an output CSV file.
- Perform data analysis on the updated dataset to ensure current data is reflected in insights.


#### Notes
- Today's updates focused on addressing the challenge of data dynamism and the need for insightful sentiment analysis visualizations.
	- The `update_csv_file` function streamlines the process of keeping our datasets up-to-date, ensuring that our sentiment analysis is based on the latest information. 
- The new visualizations in the Jupyter notebook will allow us to observe patterns and correlations within our data more effectively, facilitating a deeper understanding of sentiment trends across different platforms.
- Set the stage for integrating these updates into our regular data analysis pipeline, ensuring ongoing quality and relevance of insights.



## Development Log: [Today's Date]

#### Pipeline Refinement

- Implemented `run_create_charts()` function for improved data visualization capabilities in our analysis pipeline.

#### New Chart Visualizations

- Joint Plot: For analyzing the relationship between post subjectivity and polarity.
- Point Plot: To correlate news polarity with post polarity.
- Box Plot: To visualize the distribution of title length.
- Count Plot: To show distribution across sentiment classes.
- Pie Chart: To depict the percentage of each sentiment class visually.

#### Codebase Changes

- Added `scripts/data_visualization.py` and `utils/visualization_helper.py` to manage visualization processes.
- Produced new visualization images for enhanced data analysis communication.

#### Future To-dos

- Address data processing DAG refinement:
  - `run_get_thread()`: Load today's post data.
  - `run_get_news()`: Load today's news data.
  - `run_update_sql()`: Integrate post and news data into the MySQL database.
  - `update_csv_file()`: Export MySQL database to a CSV file.

- Plan for the integration of automated chart generation in daily data processing.

####mit Notes

- Enhanced the data visualization aspect, addressing the challenge of:
  - Visualizing complex data relationships.
  - Understanding data distributions.
  - Uncovering patterns and drawing meaningful conclusions from sentiment analysis data.
- Today's updates are set to improve stakeholder understanding and engagement with sentiment analysis results.
- Laid the groundwork for future integration into the daily analysis workflow, boosting our data storytelling abilities.

---

