FROM clojure:openjdk-11-lein
WORKDIR /opt/microservice
COPY . /opt/microservice
RUN lein uberjar
CMD ["java", "-jar", "/opt/microservice/.jar"]
