(ns simple-microservice.routes
    (:require [io.pedestal.route :as route]))

(def routes
    (route/expand-routes
        #{["/greet" :get respond-hello :route-name :greet]}))

