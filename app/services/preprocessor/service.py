from app.models import Producer, Consumer
from manager import Manager


class Service:
    def __init__(self):
        self.topics = ['preprocessed_tweets_antisemitic', 'preprocessed_tweets_not_antisemitic']
        self.topic_conversion =\
            {'raw_tweets_antisemitic': self.topics[0],
             'raw_tweets_not_antisemitic': self.topics[1]}
        self.consumer = Consumer(self.topics)
        self.producer = Producer()


    def get_service(self):
        for message in self.consumer.get_consumed_messages():
            new_document = message.value
            new_document['clean_text'] = Manager(new_document['text']).process()
            new_document['original_text'] = new_document.pop['text']
            self.producer.publish_massage(self.topic_conversion[message.topic], new_document)






