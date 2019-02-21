(ns simple-microservice.prepopulate
    (:require [simple-microservice.db.feed-diary :as feed-diary]
              [simple-microservice.db :as db]))

(defn prepopulate []
    (feed-diary/create-feed-diary-table db/db)
    (feed-diary/insert-feed db/db))