FROM clojure:openjdk-11-lein
WORKDIR /opt/microservice
COPY . /opt/microservice
RUN lein uberjar
CMD ["java", "-jar", "/opt/microservice/target/simple-microservice-0.0.1-SNAPSHOT-standalone.jar"]
