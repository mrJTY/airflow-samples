(ns simple-microservice.core
  (:require [io.pedestal.http :as http]))

(defn respond-hello [req]
  {:status 200, :body 'Hello})

(defn -main [& x]
  (println(respond-hello x)))
