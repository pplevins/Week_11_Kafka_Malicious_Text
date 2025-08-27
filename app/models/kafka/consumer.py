import json

from kafka import KafkaConsumer


class Consumer:
    def __init__(self, topic, bootstrap_servers=None):
        if bootstrap_servers is None:
            bootstrap_servers = ['localhost:9092']
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers

    def get_consumed_messages(self):
        consumer = KafkaConsumer(self.topic,
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=self.bootstrap_servers,
                                 group_id='my-group',
                                 consumer_timeout_ms=10000
                                 )
        messages = []
        for msg in consumer:
            print(msg)
            messages.append(msg.value)
        # consumer.close()
        return messages
