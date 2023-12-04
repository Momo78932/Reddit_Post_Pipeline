import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import os
current_path = os.getcwd()
repos_substring = '/Reddit_Post_Pipeline'
repos_index = current_path.find(repos_substring)
project_folder_path = current_path[:repos_index + len(repos_substring)]
sys.path.append(project_folder_path)
from utilis.mysql_helper import *
from scripts.post_sentiment_processing import *
import datetime 

with DAG(
    dag_id='update_mysql_database',
    schedule_interval='30 19 * * *',
    start_date=pendulum.datetime(2023, 12, 2, tz="EST"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['MySql', 'Reddit Post Sentiment Analysis'],
) as dag:
    update_sql_tables = PythonOperator(
        task_id = 'load_thread_mongodb',
        python_callable= run_update_sql,
    )
    check_mysql_connection = PythonOperator(
        task_id = 'check_mysql_connection',
        python_callable= check_sql_connection,
    )

check_mysql_connection >> update_sql_tables