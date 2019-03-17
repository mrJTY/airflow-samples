import time
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator



def print_hello():
    return "Hello..."

def sleep():
    time.sleep(1)

def print_world():
    return "World!"

def print_now():
    return f"It is currently...{datetime.now()}"


DAG_ID = 'hello_world_dag'

dag = DAG('hello_world', description='Simple tutorial DAG',
          schedule_interval='* * * * *',
        start_date=datetime(2017, 3, 20), catchup=False)

hello_operator = PythonOperator(python_callable = print_hello, task_id = 'hello_task', dag = dag)
sleep_operator = PythonOperator(python_callable = sleep, task_id = 'sleep_task', dag = dag)
world_operator = PythonOperator(python_callable = print_world, task_id = 'world_task', dag = dag)
now_operator = PythonOperator(python_callable = print_now, task_id = 'print_now', dag = dag)

# Task list
# =========
hello_operator >> sleep_operator >> world_operator >> now_operator
