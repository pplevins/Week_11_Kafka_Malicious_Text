

from app.models import Consumer, Producer
from enricher_manager import EnricherManager


class EnricherService:
    def __init__(self):
        self.topics = ('preprocessed_tweets_antisemitic', 'preprocessed_tweets_not_antisemitic')
        self.topic_conversion = {self.topics[0]: 'enriched_preprocessed_tweets_antisemitic',
                                 self.topics[1]: 'enriched_preprocessed_tweets_not_antisemitic'}
        self.consumer = Consumer(self.topics)
        self.producer = Producer()

    def get_service(self):
        for message in self.consumer.get_consumed_messages():
            print(message.value)
            new_document = EnricherManager(message.value).get_document()
            self.producer.publish_massage(self.topic_conversion[message.topic], new_document)



if __name__ == '__main__':
    EnricherService().get_service()
