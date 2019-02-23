(ns simple-microservice.db.feed-log
    (:require [hugsql.core :as hugsql]))

;; The path is relative to the classpath (not proj dir!),
;; so "src" is not included in the path.
;; The same would apply if the sql was under "resources/..."
;; Also, notice the under_scored path compliant with
;; Clojure file paths for hyphenated namespaces
(def feed-log-queries  "simple_microservice/db/sql/feed-log.sql")
(hugsql/def-db-fns feed-log-queries)
;;(hugsql/def-sqlvec-fns feed-diary-queries)
