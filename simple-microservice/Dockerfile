FROM clojure:openjdk-11-lein
WORKDIR /opt/microservice
COPY . /opt/microservice
RUN lein clean
RUN lein uberjar
# CMD ["lein", "run-dev"]
CMD ["java", "-jar", "/opt/microservice/target/simple-microservice-0.0.1-SNAPSHOT-standalone.jar"]