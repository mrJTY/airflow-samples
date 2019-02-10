WEBSERVER_PORT=8080
export SLUGIFY_USES_TEXT_UNIDECODE=yes
export AIRFLOW_HOME=$(shell echo `pwd`)

# Export a connection
# See: https://airflow.readthedocs.io/en/stable/howto/manage-connections.html
export AIRFLOW_CONN_POSTGRES_MASTER=postgres://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)

webserver:
	airflow webserver -p $(WEBSERVER_PORT) &

# Run a daemon scheduler
scheduler:
	airflow scheduler -D -i $(AIRFLOW_HOME)/scheduler.pid &

kill_scheduler:
	kill -9 `$(AIRFLOW_HOME)/scheduler.pid`

restart_scheduler: kill_scheduler scheduler

install: clean
	pip install apache-airflow==1.10.2 psycopg2==2.7.5 && \
	airflow initdb && \
	sed -i "s/load_examples = True/load_examples = False/" $(AIRFLOW_HOME)/airflow.cfg

uninstall:
	pip uninstall apache-airflow

clean:
	rm -f *.db \
	rm -f *.cfg
