# This Makefile is used to install Airflow on your local machine or inside a docker container.
# Usage:
#	`make install` to install the environment using conda. Assumes you have Anaconda on your system
# ` `make airflow` to start a webserver and a scheduler on the background
SHELL := /bin/bash
export WEBSERVER_PORT=8080
export CONDA_ENV=airflow_samples_env
export SLUGIFY_USES_TEXT_UNIDECODE=yes
export AIRFLOW_HOME=$(shell echo `pwd`)

# Export a connection string for Airflow to read from.
# See: https://airflow.readthedocs.io/en/stable/howto/manage-connections.html
export AIRFLOW_CONN_POSTGRES_MASTER=postgres://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)

airflow:
	airflow scheduler -D --pid $(AIRFLOW_HOME)/scheduler.pid &
	airflow webserver -p $(WEBSERVER_PORT)

install: clean
	pip install apache-airflow==1.10.2 psycopg2==2.7.5 && \
	airflow initdb && \
	sed -i "s/load_examples = True/load_examples = False/" $(AIRFLOW_HOME)/airflow.cfg && \
	airflow resetdb -y

kill-scheduler:
	kill -9 `$(AIRFLOW_HOME)/scheduler.pid`

restart-scheduler: kill_scheduler scheduler

uninstall: clean
	pip uninstall airflow

clean:
	rm -f *.db \
	rm -f *.cfg
