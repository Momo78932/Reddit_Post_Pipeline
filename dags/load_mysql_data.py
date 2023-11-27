import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from scripts.get_reddit_thread import run_get_thread
from utilis.redis_helper import check_redis_connection
from utilis.mongodb_helper import check_mongodb_connection
from scripts.post_sentiment_processing import *
import datetime 

with DAG(
    dag_id='load_mysql_thread',
    schedule_interval='0 21 * * *',
    start_date=pendulum.datetime(2023, 11, 25, tz="EST"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['MySQL',  'Reddit Post Sentiment Analysis'],
) as dag:
    check_mdb_connction = PythonOperator(
        task_id = 'check_mongodb_connection',
        python_callable= check_mongodb_connection,
    )
    check_mysql_connction = PythonOperator(
        task_id = 'check_MySQL_connection',
        python_callable= check_sql_connection,
    )
    load_thread_to_sql = PythonOperator(
        task_id = 'load_thread_mysql',
        python_callable= run_update_sql,
    )



[check_mdb_connction, check_mysql_connction]  >> load_thread_to_sql