(ns simple-microservice.service
  (:require [io.pedestal.http :as http]
            [io.pedestal.http.route :as route]
            [io.pedestal.http.body-params :as body-params]
            [simple-microservice.db.feed-log :as feed-log]
            [simple-microservice.db :as db]
            [ring.middleware.json :as ring-json]
            [ring.util.response :as ring-resp]))

(def port 9090)

(defn about-page
  [request]
  (ring-resp/response (format "Clojure %s - served from %s"
                              (clojure-version)
                              (route/url-for ::about-page))))

(defn home-page
  [request]
  (ring-resp/response "Hello World!"))

;; Get the most recent feed logs
(defn list-feed-logs
  [request]
  (http/json-response (feed-log/list-feed-logs db/db)))

;; Get the most recent feed logs for a pet
(defn list-feed-logs-for-a-pet
  [request]
  (let [pet-name (get-in request [:path-params :name])]
    (http/json-response (feed-log/list-feed-logs-for-a-pet db/db {:name pet-name}))))

;; Post a new feed log for a pet
(defn post-feed-log
  [request]
  (let [pet-name (get-in request [:json-params :name])
        date-fed (get-in request [:json-params :datetimestamp])]
     (feed-log/insert-feed-log db/db {:name pet-name :datetimestamp date-fed})
     (http/json-response {:name pet-name :datetimestamp date-fed})))

(def common-interceptors [(body-params/body-params) http/html-body])
(def json-interceptor [(body-params/body-params) http/json-body])

;; Tabular routes
(def routes #{["/"               :get  (conj common-interceptors `home-page)]
              ["/about"          :get  (conj common-interceptors `about-page)]
              ["/feedlog"        :get  (conj json-interceptor `list-feed-logs)]
              ["/feedlog/:name"  :get  (conj json-interceptor `list-feed-logs-for-a-pet)]
              ["/feedlog"        :post (conj json-interceptor `post-feed-log)]})

(def service
  {::http/routes routes
   ::http/host  "0.0.0.0"
   ::http/type  :jetty
   ::http/port  port})

