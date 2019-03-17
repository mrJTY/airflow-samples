# Airflow demonstration

This demonstration is meant to showcase Airflow's features.


# Getting started

The docker compose script will setup the following containers for demonstration:

1) Airflow - to be used for orchestrating the workflows (Python3 container)
2) A backend database in Postgres - this will be used for storing some data (Postgres container)
3) A simple microservice in Clojure - to be used for interacting with the backend database (Clojure container)

In a terminal run:

```bash
# Start the Docker daemon if needed
sudo dockerd

# Start up stack, use the build flag if needed
sudo docker-compose up --build
```

# Airflow UI

Visit http://localhost:8080 to view the admin panel that will orchestrate the workflows.

# Microservice API

```
PUT 
```

