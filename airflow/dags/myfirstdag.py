from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello...'

def print_world():
    return "World!"

dag = DAG('hello_world', description='Simple tutorial DAG. I am meant to run every minute!',
        schedule_interval='* * * * *',
        start_date=datetime(2017, 3, 20), catchup=False)


hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
world_operator = PythonOperator(task_id='world_task', python_callable=print_world, dag=dag)
hello_operator >> world_operator