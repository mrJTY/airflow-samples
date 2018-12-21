
# AIRFLOW_HOME:
export AIRFLOW_HOME=$(shell echo `pwd`)

initdb:
	airflow initdb

webserver:
	airflow webserver -p 8080

scheduler:
	airflow scheduler

clean:
	rm *.db \
	rm -rf logs \
	rm *.cfg