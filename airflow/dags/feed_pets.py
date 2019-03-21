import time
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import random
import logging
import os
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators import SimpleHttpOperator

# Default dag settings
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # Start from yesterday for demonstration
    'start_date': datetime.utcnow() - timedelta(days = 5),
    'email': ['alertreceiver@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(seconds = 2),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

# In this case, we are simply defining a connection ID based on environment variables passed from Docker Compose
# https://airflow.readthedocs.io/en/stable/howto/manage-connections.html
HTTP_CONN_ID = "HTTP_CONN"
POSTGRES_CONN_ID = "POSTGRES_CONN"
POSTGRES_DB = "db"

# Setup a DAG
# =============
dag = DAG('feed_pets_dag',
        description = 'Simple tutorial DAG',
        schedule_interval = '0 7 * * *',
        default_args = default_args)


# Fetch food
# ============
def fetch_food():
    logging.info("Fetching food...")
    time.sleep(2)
    logging.info("Food fetched!")
    return "We got food!"

fetch_food_operator = PythonOperator(python_callable = fetch_food, task_id = 'fetch_food', dag = dag)

# Try to open a can
# ==================
def open_food():
    logging.info("Attempting to open a can of pet food...")
    prob_of_failure = 0.3

    if random.random() < prob_of_failure:
        logging.warning("Doh! Can't open can!")
        raise Exception("Doh! Can't open can!")
    else:
        logging.info("Succesfully opened can!")

open_food_operator = PythonOperator(python_callable = open_food, task_id = 'open_food', dag = dag)



# https://airflow.apache.org/_modules/airflow/operators/http_operator.html
# https://github.com/trbs/airflow-examples/blob/master/dags/example_http_operator.py


# Log the feeding diary for analysis via microservice
# =================================================
pet_name = "doge"
post_feed_log = SimpleHttpOperator(
    task_id='post_op',
    http_conn_id = HTTP_CONN_ID,
    endpoint='feedlog',
    # Ds is current execution macro variable: http://airflow.apache.org/code.html#default-variables
    data = f"name={pet_name}&datetimestamp=" + "{{ ds }}",
    headers = {"Content-Type": "application/x-www-form-urlencoded"},
    dag=dag)

# Analyse FeedDiary postgres
# ===========================================
analyse_query = f"""
select
    name
    , count(distinct feed_id) as count_of_feeds_to_date
    , max(datetimestamp) as last_feed
from
    feed_log
group by
    name
"""
analyse_operator = PostgresOperator(task_id = 'analyse_feeds',
                                    sql = analyse_query,
                                    dag = dag,
                                    autocommit = True,
                                    postgres_conn_id = POSTGRES_CONN_ID,
                                    database = POSTGRES_DB)


# Define dependencies
# ===================
fetch_food_operator >> open_food_operator >> post_feed_log >>analyse_operator
