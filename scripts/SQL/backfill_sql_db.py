import configparser
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from scripts.SQL.interact_with_sql_db_query import *
from scripts.post_sentiment_processing import *
from utilis.redis_helper import *
from utilis.settings import *
from datetime import datetime, timedelta
from utilis.mongodb_helper import mongodb_connection, mongodb_cred

# Set the start date and end date
start_date_str = '2023-11-09'
end_date = datetime.now() - timedelta(days=1) 
start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

# Generate a list of dates from the start date to one day before today (yesterday)
date_list = [(start_date + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, (end_date - start_date).days + 1)]


# implement backfill
for date in date_list:
    mysql_connection = mysql.connector.connect(
        host=Configs['mysql_cred']['host'],       
        database= mysql_database,
        user=Configs['mysql_cred']['user'],     
        password=Configs['mysql_cred']['password'] 
    )
    update_sql_db(mysql_connection, mysql_database, mongodb_info['mgdb_db_name'], mongodb_info['mgdb_collection_name'], date)



