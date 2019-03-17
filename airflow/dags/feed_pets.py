import time
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import random
import logging
import os
from airflow.operators.postgres_operator import PostgresOperator

# In this case, we are simply defining a connection ID based on an environment variable
# https://airflow.readthedocs.io/en/stable/howto/manage-connections.html
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_CONN_ID = f"postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

# Setup a DAG
# =============
dag = DAG('feed_pets_dag',
        description = 'Simple tutorial DAG',
        # Feed them every 6th hour from 7am - 7pm. Ie: 07:00, 13:00, 19:00
        schedule_interval = '0 7-19/6 * * *',
        # If any task fails, retry 3 times
        retries = 3,
        start_date = datetime.utcnow(),
        catchup = False)


# Fetch food
# ============
def fetch_pet_food():
    logging.info("Fetching food...")
    time.sleep(2)
    logging.info("Food fetched!")
    return "We got food!"

fetch_pet_food_operator = PythonOperator(python_callable = fetch_pet_food, task_id = 'fetch_pet_food', dag = dag)

# Try to open a can
# ==================
def open_pet_food():
    logging.info("Attempting to open a can of pet food...")
    prob_of_failure = 0.3

    if random.random() < prob_of_failure:
        logging.warning("Doh! Couldn't open can!")
    else:
        logging.info("Succesfully opened can!")

open_pet_food_operator = PythonOperator(python_callable = open_pet_food, task_id = 'open_pet_food', dag = dag)

# Log the feeding diary for analysis via microservice
# =================================================
# log_to_feeding_diary_operator = HTTPOperator()

# Analyse FeedDiary postgres
# ===========================================
analyse_query = f"""
select
    name
    , count(distinct feed_id) as count_of_feeds_to_date
    , max(datetimestamp) as last_feed
from
    feed_diary
group by
    name
"""
analyse_operator = PostgresOperator(task_id = 'analyse_diary', sql = analyse_query, dag = dag, autocommit = True, postgres_conn_id = POSTGRES_CONN_ID, database = POSTGRES_DB)


# Define dependencies
# ===================
fetch_food_operator >> open_pet_food_operator >> log_to_feeding_diary_operator >> analyse_operator
