(ns simple-microservice.routes
    (:require [io.pedestal.http.route :as route]))

(defn respond-hello [req]
  {:status 200 :body "Hello"})

(def routes
    (route/expand-routes
        #{["/greet" :get respond-hello :route-name :greet]}))

