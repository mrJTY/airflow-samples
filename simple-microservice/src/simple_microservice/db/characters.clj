(ns simple-microservice.db.characters
    (:require [hugsql.core :as hugsql]))

;; The path is relative to the classpath (not proj dir!),
;; so "src" is not included in the path.
;; The same would apply if the sql was under "resources/..."
;; Also, notice the under_scored path compliant with
;; Clojure file paths for hyphenated namespaces
(def characters-file  "simple_microservice/db/sql/characters.sql")
(hugsql/def-db-fns characters-file)
(hugsql/def-sqlvec-fns characters-file)