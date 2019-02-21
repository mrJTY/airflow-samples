FROM clojure:openjdk-11-lein
ADD target/simple-microservice-0.0.1-SNAPSHOT-standalone.jar /simple-microservice/app.jar
RUN lein uberjar
CMD ["java", "-jar", "/simple-microservice/app.jar"]
