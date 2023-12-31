import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
sys.path.append('/Users/liuminghuang/Repos/Reddit_Post_Pipeline')
from scripts.get_reddit_thread import run_get_thread
# from utilis.redis_helper import check_redis_connection
# from utilis.mongodb_helper import check_mongodb_connection


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
    # check_rds_connection = PythonOperator(
    #     task_id = 'check_redis_connection',
    #     python_callable= check_redis_connection,
    # )
    # check_mdb_connction = PythonOperator(
    #     task_id = 'check_mongodb_connection',
    #     python_callable= check_mongodb_connection,
    # )


load_thread