PING

INFO



SET k1 v1
GET k1
<!-- string -->


LPUSH list1 node1
LRANGE listname 0 -1
<!-- list -->


SADD users admin
SADD users vae
<!-- set -->

ZADD comments 2020 "c1"
ZADD comments 2021 "c2"


HSET user:vae job "music" city "beijing"
HGETALL
HGET user:vae job

HSET comments:c1 content "great" user "vae"
