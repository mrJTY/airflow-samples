from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now() - timedelta(days = 1),
    'email': ['your-email@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'email_on_success': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
    'catchup': False
}

# Connection string as defined in the Makefile
POSTGRES_CONN_ID = 'POSTGRES_MASTER'
POSTGRES_DB = "db"
dag = DAG('tutorial', default_args = default_args, schedule_interval = '0 0 * * *')

# Create cats table
# =======================
create_pets_table_query = """
create table Pets(
    PetId   bigint,
    PetName varchar(32),
    WeightKg  float
);
"""
create_pets_table_task = PostgresOperator(task_id = 'create_pets_table', sql = create_pets_table_query, autocommit = True, postgres_conn_id = POSTGRES_CONN_ID, database = POSTGRES_DB)

# Fill in some sample data
# =======================
insert_cats_query = """
insert into Pets values
(1, "Boots", 7.5),
(2, "Loki", 4.5),
(3, "Lucy", 2.1)
"""
insert_cats_tasks = PostgresOperator(task_id = 'insert_cats', sql = insert_cats_query, autocommit = True, postgres_conn_id = POSTGRES_CONN_ID, database = POSTGRES_DB)

# TODO: Query the data

# TODO: call clojure to do some operation using an endpoint

# TODO: Query the data


# Tasks chaining
# ==============
create_pets_table_task >> insert_cats_tasks