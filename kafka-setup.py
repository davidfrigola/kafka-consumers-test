from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='test'
)


topic_list = []
topic_list.append(NewTopic(name="poc-topic", num_partitions=2, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

# Use this to delete the topic 
#admin_client.delete_topics(['poc-topic'], timeout_ms=10000)
