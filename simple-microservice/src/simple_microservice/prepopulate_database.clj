(ns simple-microservice.prepopulate-database
    (:require [simple-microservice.db.feed-log :as feed-log]
              [simple-microservice.db :as db]))

(defn prepopulate-database []
    (println "Prepopulating feed_log table")
    (feed-log/create-feed-log-table db/db)
    (feed-log/insert-feed-log db/db {:name "phish" :datetimestamp "2019-01-01"}))
