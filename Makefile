build-clj-microservice:
	cd simple-microservice && lein uberjar

docker-compose-build: build-clj-microservice
	docker-compose build

all: docker-compose-build
	docker-compose up