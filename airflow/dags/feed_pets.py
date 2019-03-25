import time
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import random
import logging
import os
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.http_operator import SimpleHttpOperator

# Default dag settings
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # Start from yesterday for demonstration
    'start_date': datetime.utcnow() - timedelta(days = 7),
    'email': ['alertreceiver@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds = 2)
}

# In this case, we are simply defining a connection ID based on environment variables passed from Docker Compose
# https://airflow.readthedocs.io/en/stable/howto/manage-connections.html
HTTP_CONN_ID = 'HTTP_CONN'
POSTGRES_CONN_ID = 'POSTGRES_CONN'
POSTGRES_DB = os.getenv('POSTGRES_DB')
PET_NAMES = ['doge', 'kitty', 'phish']

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
def try_feed():
    logging.info("Attempting to feed a pet...")
    prob_of_failure = 0.5

    if random.random() < prob_of_failure:
        logging.warning("Refused! Picky pet...")
        raise Exception("Refused! Picky pet...")
    else:
        logging.info("Succesfully fed!")

try_feed_operator = PythonOperator(python_callable = try_feed, task_id = 'try_feed_pet', dag = dag)


# Use the ds macro variable to get the dag's runtime in yyyy-mm-dd
# https://airflow.apache.org/_modules/airflow/operators/http_operator.html
# https://github.com/trbs/airflow-examples/blob/master/dags/example_http_operator.py


# Log the feeding diary for analysis via microservice
# =================================================
pet_name = random.choice(PET_NAMES)
mark_db_operator = SimpleHttpOperator(
    task_id='mark_success_to_db',
    http_conn_id = HTTP_CONN_ID,
    method = "POST",
    # Ds is current execution macro variable: http://airflow.apache.org/code.html#default-variables
    endpoint = 'feedlog' + f"?name={pet_name}&datetimestamp=" + "{{ ds }}",
    dag=dag)

# Create a fact table
# ===========================================
query = f"""
begin;
drop table if exists fact_analytics;
-- Just for demonstration... ideally this should just be inserting to the same table and not destroying it
create table fact_analytics as
select
    name
    , count(1) as count_of_feeds
    , max(datetimestamp) as last_feed
from
    feed_log
group by
    name
order by
    name, last_feed desc
;
end;
"""

create_fact_table_operator = PostgresOperator(task_id = 'create_fact_table',
                                    sql = query,
                                    dag = dag,
                                    autocommit = True,
                                    postgres_conn_id = POSTGRES_CONN_ID,
                                    database = POSTGRES_DB)

# Define dependencies
# ===================
fetch_food_operator >> try_feed_operator >> mark_db_operator >> create_fact_table_operator
