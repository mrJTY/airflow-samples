from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Let us introduce some bad code...
# ==================================
dag = DAG('buggy_dag',
    description='Sh*t dag',
    schedule_interval='* * * * *',
    start_date=datetime(2017, 3, 20), catchup=False)

def buggy_code():
    return f"I am a bad peice of code.....{0/0}"

def print_hello():
    return "Hello..."

hello_operator = PythonOperator(python_callable = buggy_code, task_id = 'hello_buggy_task', dag = dag)
buggy_operator = PythonOperator(python_callable = buggy_code, task_id = 'buggy_task', dag = dag)

# Task list
# =========
hello_operator >> buggy_operator