#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from json import dumps, loads
from datetime import datetime
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer, KafkaProducer, TopicPartition

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9091")
consumer = KafkaConsumer("topic_test", bootstrap_servers=["localhost:9091"], auto_offset_reset='latest', enable_auto_commit=True, group_id='my-group', value_deserializer=lambda x: loads(x.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers=["localhost:9091"], value_serializer=lambda x: dumps(x).encode('utf-8'))

topics_list = consumer.topics()
if len(topics_list) == 0:
  new_topics_list = []
  new_topics_list.append(NewTopic(name="topic_test", num_partitions=2, replication_factor=1))
  admin_client.create_topics(new_topics=new_topics_list, validate_only=False)

print(admin_client.describe_topics(topics=["topic_test"]))

producer.send("topic_test", value={ 'test': 'test' })

partitions = [TopicPartition("topic_test", p) for p in consumer.partitions_for_topic("topic_test")]
print(partitions)
timestamps = {p: 1609799391301 for p in partitions}
print(consumer.offsets_for_times(timestamps))

for message in consumer:
  print(message)
