(ns simple-microservice.db.feed-log
    (:require [hugsql.core :as hugsql]))

(def feed-log-queries  "simple_microservice/db/sql/feed_log.sql")
(hugsql/def-db-fns feed-log-queries)
