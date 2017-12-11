from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect()
create_keyspace = "CREATE KEYSPACE IF NOT EXISTS Transport_keyspace" \
                  " WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':1};"
create_table_transport = """

CREATE TABLE transport(
   head_rt_version double PRIMARY KEY,
   head_time_stamp timestamp,
   head_user_data varchar,
   id varchar,
   is_deleted Boolean,
   trip_id bigint,
   route_id int,
   start_date date,
   schedule_relationship int,
   vehicle_id int,
   vehicle_label int,
   latitude double,
   longitude double,
   bearing int,
   odometer float,
   speed float,
   current_stop_sequence int,
   current_status int,
   vehicle_time_stamp timestamp,
   vehicle_congestion_level int
   )

"""
print(session.execute(create_keyspace))
print(session.execute("use Transport_keyspace"))
print(session.execute(create_table_transport))