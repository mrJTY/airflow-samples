(ns simple-microservice.core
  (:require [io.pedestal.http :as http]
            [simple-microservice.routes :as routes]))


(defn create-server []
  (http/create-server
    { ::http/routes routes/routes
      ::http/type   :jetty
      ::http/port   8890}))

(defn start []
  (http/start (create-server)))

(defn -main [& x]
  (start))
