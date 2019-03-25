# Airflow demonstration

This demonstration is meant to showcase Airflow's features.


# Quickstart

Quick start script assuming you have Docker daemon running in the background

```bash
./bin/start.sh
```

The docker compose script will setup the following containers for demonstration:

1) Airflow - to be used for orchestrating the workflows (Python3 container)
2) Postgres - this will be used for storing some data (Postgres container)
3) Simple Microservice in Clojure - to be used for interacting with the backend database (Clojure container)
3) Jupyter Notebook - for visual analytics


To start manually:

```bash
# Start the Docker daemon if needed
sudo dockerd

# Start up stack, use the build flag if needed
# Suggest to rebuild each time there is a change in the dags folder
sudo docker-compose up --build
```

# Airflow UI

Visit http://localhost:8080 to view the admin panel that will orchestrate the workflows.

# Visual Analytics

Visit http://localhost:8888. If prompted for password, type `password`.

(Not the best security but this is just a demo! See the jupyter config, there is a password hash there that can be changed)

# Microservice API

These are the routes for the simple feed microservice

## Get top 10 most recent feed logs for all pets

```bash
curl "http://localhost:9090/feedlog"
```

## Post a feed log for a pet

```bash
curl -X POST --header "Content-Type: application/json" --data '{"name":"doge","datetimestamp":"2019-01-01"}' "http://localhost:9090/feedlog" 
```

## Get top 10 most recent logs for Doge

```bash
$ curl "http://localhost:9090/feedlog/doge"
[{:id 1, :name "doge", :datetimestamp #inst "2019-03-17T13:10:58.676240000-00:00"}]
```
