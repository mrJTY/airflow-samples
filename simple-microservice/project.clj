(defproject simple-microservice "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :main simple-microservice.core
  :dependencies [[org.clojure/clojure "1.8.0"]
                [io.pedestal/pedestal.service       "0.5.1"]
                [io.pedestal/pedestal.jetty         "0.5.1"]
                [io.pedestal/pedestal.route         "0.5.1"]
                [org.slf4j/slf4j-simple             "1.7.21"]])
