(ns simple-microservice.scratch
    (:require [simple-microservice.db.characters :as characters]
              [io.pedestal.test :as test]
              [simple-microservice.db :as db]
            [io.pedestal.http.route :as route]
            [io.pedestal.http.body-params :as body-params]
            [simple-microservice.service  :as service]
            [ring.util.response :as ring-resp]))

(test/response-for service/home-page :get)