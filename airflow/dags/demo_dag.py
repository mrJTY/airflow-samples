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
create_cats_table_query = """
create table Cats(
    CatId   bigint,
    CatName varchar(32)
);
"""
create_cats_table_task = PostgresOperator(sql = create_cats_table_query, autocommit = True, postgres_conn_id = POSTGRES_CONN_ID, database = POSTGRES_DB)

# Fill in some sample data
# =======================
insert_cats_query = """
insert into Cats values
(1, "Boots"),
(2, "Loki"),
(3, "Lucy")
"""
insert_cats_tasks = PostgresOperator(sql = insert_cats_query, autocommit = True, postgres_conn_id = POSTGRES_CONN_ID, database = POSTGRES_DB)

# TODO: Query the data

# TODO: call clojure to do some operation using an endpoint

# TODO: Query the data


# Tasks chaining
# ==============
create_cats_table_task >> insert_cats_tasks