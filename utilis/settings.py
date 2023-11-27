from datetime import datetime, timedelta
default_date = datetime.today().strftime('%Y-%m-%d')
mysql_database = "testing"
reddit_info = {
    'userAgentName': 'airflow',
    'subredditName': 'ChatGPT',
    'numSubreddit': 40,
}
redis_info = {
    'rds_port': '6379',
    'rds_dbNum': 1,
    'rds_host': 'localhost',
    'rds_key': 'reddit_title_id'
}
mongodb_info = {
    'mgdb_db_name': 'chatgpt_reddit_thread',
    'mgdb_collection_name': 'top_posts'
}