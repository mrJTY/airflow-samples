
-- :name create-feed-log-table
-- :command :execute
-- :result :raw
-- :doc Create characters table
--  H2 Database specific (adjust to your DB)
create table if not exists feed_log (
  id         serial primary key,
  name       varchar(40),
  datetimestamp timestamp not null default current_timestamp
)

-- A ":result" value of ":*" specifies a vector of records
-- (as hashmaps) will be returned
-- :name list-feed-logs :? :*
-- :doc Get all feed log
select * from feed_log
order by id
limit 10

-- A ":result" value of ":*" specifies a vector of records
-- (as hashmaps) will be returned
-- :name list-feed-log-for-a-pet :? :*
-- :doc Get all feed log
select * from feed_log
where name = :name
order by datetimestamp desc
limit 10

-- A :result value of :n below will return affected rows:
-- :name insert-feed-log :! :n
-- :doc Insert a single character returning affected row count
insert into feed_log (name)
values (:name)

