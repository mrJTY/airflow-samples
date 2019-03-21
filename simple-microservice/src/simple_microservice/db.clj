(ns simple-microservice.db)

;; Connection id's to connect to postgres db
(def db_host_name "postgreshost")
(def db_port 5432)
(def db_name "")
(def db_user "postgres")
(def db_password "password123")

(def db
    {
    :classname "org.postgresql.Driver"
    :subprotocol "postgresql"
    :subname (str "//" db_host_name ":" db_port"/")
    :user db_user
    :password db_password})


