from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import random

# Let us introduce some bad code...
# ==================================
dag = DAG('buggy_dag',
    description='buggy dag',
    schedule_interval='* * * * *',
    retries = 5,
    start_date=datetime.utcnow(), catchup=False)

def buggy_code():
    """
    Buggy task that may fail half the time!
    """
    if random.random() < 0.5:
        raise Exception("Failed!")
    else:
        return "Success!"

def print_hello():
    return "Hello..."

hello_operator = PythonOperator(python_callable = buggy_code, task_id = 'hello_buggy_task', dag = dag)
buggy_operator = PythonOperator(python_callable = buggy_code, task_id = 'buggy_task', dag = dag)

# Task list
# =========
hello_operator >> buggy_operator
