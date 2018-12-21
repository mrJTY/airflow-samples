echo $AIRFLOW_HOME
cd $AIRFLOW_HOME

airflow initdb
airflow scheduler &
airflow webserver -p 8080