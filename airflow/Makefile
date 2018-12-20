
# AIRFLOW_HOME:
export AIRFLOW_HOME=$(shell echo `pwd`)

initdb:
	echo $$AIRFLOW_HOME && airflow initdb

webserver: initdb
	airflow webserver -p 8080

scheaduler: initdb
	airflow scheduler

clean:
	rm *.db \
	rm -rf logs \
	rm *.cfg