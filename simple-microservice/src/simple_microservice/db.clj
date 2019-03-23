(ns simple-microservice.db)

;; Connection id's to connect to postgres db
(def db_host_name (or (System/getenv "POSTGRES_HOST") "postgreshost"))
(def db_port (or (System/getenv "POSTGRES_PORT") 5432))
(def db_name (or (System/getenv "POSTGRES_DB") "db"))
(def db_user (or (System/getenv "POSTGRES_USER") "postgres"))
(def db_password (or (System/getenv "POSTGRES_PASSWORD") "password123"))

(def db
    {
    :classname "org.postgresql.Driver"
    :subprotocol "postgresql"
    :subname (str "//" db_host_name ":" db_port "/" db_name)
    :user db_user
    :password db_password})


