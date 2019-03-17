from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import random

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # Start from yesterday for demonstration
    'start_date': datetime.utcnow() - timedelta(days = 1),
    'email': ['alertreceiver@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 10,
    'retry_delay': timedelta(seconds = 2),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}


# Let us introduce some bad code...
# ==================================
dag = DAG('buggy_dag',
    description = 'buggy dag',
    schedule_interval = '* * * * *',
    default_args = default_args)

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
