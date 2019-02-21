# Call a microservice to feed pets. Scheduled 3 times a day
from airflow.models import DAG

DAG = DAG()

# Fetch cans
fetch_operator = PythonOperator()

# Try an open
open_operator = PythonOperator

# Try a serve, pet may refused
serve_operator = 

# If consumed, mark as done on FeedDiary via Clojure microservice
mark_as_done = HTTPOperator()

# Analyse FeedDiary postgres

analyse = PostgresOperator