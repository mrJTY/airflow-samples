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
  (ring-resp/response (feed-log/list-feed-logs db/db)))

;; Get the most recent feed logs for a pet
(defn list-feed-logs-for-a-pet
  [request]
  (let [pet-name (get-in request [:path-params :name])]
    (ring-resp/response (feed-log/list-feed-logs-for-a-pet db/db {:name pet-name}))))

;; Post a new feed log for a pet
(defn post-feed-log
  [request]
  (let [pet-name (get-in request [:query-params :name])]
     (feed-log/insert-feed-log db/db {:name pet-name})
     (ring-resp/response (str "insert " pet-name))))

(def common-interceptors [(body-params/body-params) http/html-body])

;; Tabular routes
(def routes #{["/"               :get  (conj common-interceptors `home-page)]
              ["/feedlog"        :get  (conj common-interceptors `list-feed-logs)]
              ["/feedlog/:name"  :get  (conj common-interceptors `list-feed-logs-for-a-pet)]
              ["/feedlog"        :post (conj common-interceptors `post-feed-log)]
              ["/about"          :get  (conj common-interceptors `about-page)]})

;; Consumed by simple-microservice.server/create-server
;; See http/default-interceptors for additional options you can configure
;; (def service {:env :prod
;;               ::http/routes routes
;;               ::http/port port
;;               ::http/type :jetty
;;               })
(def service
  {::http/routes routes
   ::http/type   :jetty
   ::http/port   port})


;;::http/join? false
;;::http/resource-path "/public"
;; all origins are allowed in dev mode
;;::http/allowed-origins {:creds true :allowed-origins (constantly true)}
;; Content Security Policy (CSP) is mostly turned off in dev mode
;;::http/secure-headers {:content-security-policy-settings {:object-src "'none'"}}
