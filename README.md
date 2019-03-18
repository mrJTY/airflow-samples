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
# Suggest to rebuild each time there is a change in the dags folder
sudo docker-compose up --build
```

# Airflow UI

Visit http://localhost:8080 to view the admin panel that will orchestrate the workflows.

# Microservice API

These are the routes

## Get top 10 most recent feed logs for all pets

```
curl -v "http://localhost:9090/feedlog"
```

## Post a feed log for a pet

```
curl -v -X POST "http://localhost:9090/feedlog?name=doge"
```

## Get top 10 most recent logs for Doge

```
curl -v "http://localhost:9090/feedlog/doge"
```

## Example

```
$ curl -X POST  "localhost:9090/feedlog?name=doge"
insert doge

$ curl -v localhost:9090/feedlog/doge             
*   Trying ::1...
* TCP_NODELAY set
* connect to ::1 port 9090 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 9090 (#0)
> GET /feedlog/doge HTTP/1.1
> Host: localhost:9090
> User-Agent: curl/7.64.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Sun, 17 Mar 2019 13:11:10 GMT
< Strict-Transport-Security: max-age=31536000; includeSubdomains
< X-Frame-Options: DENY
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< X-Download-Options: noopen
< X-Permitted-Cross-Domain-Policies: none
< Content-Security-Policy: object-src 'none'; script-src 'unsafe-inline' 'unsafe-eval' 'strict-dynamic' https: http:;
< Content-Type: application/edn
< Transfer-Encoding: chunked
< 
* Connection #0 to host localhost left intact
({:id 1, :name "doge", :datetimestamp #inst "2019-03-17T13:10:58.676240000-00:00"})% 
```
