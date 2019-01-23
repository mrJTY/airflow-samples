FROM clojure:openjdk-8-lein

ENV HOME /opt/simple-microservice
WORKDIR ${HOME}

COPY . .

CMD ["lein", "run", "main"]