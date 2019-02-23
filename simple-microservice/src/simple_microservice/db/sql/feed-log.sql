
-- :name create-feed-log-table
-- :command :execute
-- :result :raw
-- :doc Create characters table
--  H2 Database specific (adjust to your DB)
create table feed_log (
  id         serial primary key,
  name       varchar(40),
  datetimestamp timestamp not null default current_timestamp
)

/* ...snip... */

-- A :result value of :n below will return affected rows:
-- :name insert-feed :! :n
-- :doc Insert a single character returning affected row count
insert into feed_log (name)
values (:name)

