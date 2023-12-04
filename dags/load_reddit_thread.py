import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import os
# Get the current working directory
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]

sys.path.append(project_folder_path)
from scripts.get_reddit_thread import *
from utilis.redis_helper import *
from utilis.mongodb_helper import *
import datetime 

with DAG(
    dag_id='load_reddit_thread',
    schedule_interval='0 19 * * *',
    start_date=pendulum.datetime(2023, 11, 13, tz="EST"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['Redis', 'Mongodb', 'Reddit Post Sentiment Analysis'],
) as dag:
    load_thread = PythonOperator(
        task_id = 'load_thread_mongodb',
        python_callable= run_get_thread,
    )
    check_rds_connection = PythonOperator(
        task_id = 'check_redis_connection',
        python_callable= check_redis_connection,
    )
    check_mdb_connction = PythonOperator(
        task_id = 'check_mongodb_connection',
        python_callable= check_mongodb_connection,
    )
    



[check_mdb_connction, check_rds_connection] >> load_thread 