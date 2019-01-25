(ns simple-microservice.routes
    (:require [io.pedestal.http.route :as route]))

(def unmentionables #{"voldemort"})

(defn respond-hello [req]
  (let [nm (get-in req [:query-params :name])
        resp (if (empty? name) "Hello there!" (str "Hello, " name "!\n")) ]
        {:status 200 :body resp}))

(def routes
    (route/expand-routes
        #{["/greet" :get respond-hello :route-name :greet]}))

