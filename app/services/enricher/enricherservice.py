from app.models import Consumer, Producer
from enrichermanager import EnricherManager


class EnricherService:
    def __init__(self):
        self.topics = ('enriched_preprocessed_tweets_antisemitic','enriched_preprocessed_tweets_not_antisemitic')
        self.topic_conversion = {'preprocessed_tweets_antisemitic':self.topics[0],'preprocessed_tweets_not_antisemitic': self.topics[1]}
        self.consumer = Consumer(self.topics)
        self.producer = Producer()

    def get_service(self):
        for message in self.consumer.get_consumed_messages():
            new_document = EnricherManager(message.value).process()
            self.producer.publish_massage(self.topic_conversion[message.topic], new_document)


if __name__ == '__main__':
    EnricherService().get_service()
