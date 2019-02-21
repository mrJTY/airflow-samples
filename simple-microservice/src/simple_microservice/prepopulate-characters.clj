(ns simple-microservice.prepopulate
  (:require [simple-microservice.db.characters :as characters]
            [simple-microservice.db :as db]))

(defn prepopulate []
  (characters/create-characters-table db/db)
  (characters/insert-character db/db {:name "Westley", :specialty "defense" })
  (characters/insert-character db/db {:name "Snap", :specialty "attack" })
  (characters/characters-by-ids-specify-cols db/db  {:ids [1 2] :cols ["name" "specialty"]}))