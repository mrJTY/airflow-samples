CONDAENV=my_airflow_env
PORT=8080
export SLUGIFY_USES_TEXT_UNIDECODE=yes
export AIRFLOW_HOME=$(shell echo `pwd`)

initdb:
	airflow initdb

webserver:
	airflow webserver -p $(PORT)

scheduler:
	airflow scheduler

install-local:
	conda create -y -n $(CONDAENV) python=3.6 && \
	source activate $(CONDAENV) && \
	pip install apache-airflow

uninstall:
	conda remove --name $(CONDAENV) --all

clean:
	rm -f *.db \
	rm -rf log \
	rm -f *.cfg

docker-compose-up: docker-compose-down
	docker-compose build && docker-compose up

docker-compose-down:
	docker-compose stop && docker-compose down