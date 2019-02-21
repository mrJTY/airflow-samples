
-- :name create-characters-table
-- :command :execute
-- :result :raw
-- :doc Create characters table
--  H2 Database specific (adjust to your DB)
create table feed_diary (
  id         serial primary key,
  name       varchar(40),
  datetimestamp timestamp not null default current_timestamp
)

/* ...snip... */

-- A :result value of :n below will return affected rows:
-- :name insert-character :! :n
-- :doc Insert a single character returning affected row count
insert into feed_diary (name)
values (:name)


-- A ":result" value of ":1" specifies a single record
-- (as a hashmap) will be returned
-- :name character
-- :doc Get character
select * from characters limit 10
