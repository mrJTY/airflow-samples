(ns simple-microservice.prepopulate
    (:require [simple-microservice.db.feed-log :as feed-log]
              [simple-microservice.db :as db]))

(defn prepopulate-database []
    (feed-log/create-feed-log-table db/db))
