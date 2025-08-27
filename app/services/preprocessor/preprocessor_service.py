from app.models import Producer, Consumer
from preprocessor_manager import PreprocessorManager


class PreprocessorService:
    def __init__(self):
        self.topics = ['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic']
        self.topic_conversion =\
            {self.topics[0]:'preprocessed_tweets_antisemitic',
             self.topics[1]:'preprocessed_tweets_not_antisemitic'}
        self.consumer = Consumer(self.topics)
        self.producer = Producer()


    def get_service(self):
        for message in self.consumer.get_consumed_messages():
            print(message.value)
            new_document = message.value
            new_document['clean_text'] = PreprocessorManager(new_document['original_text']).process()
            self.producer.publish_massage(self.topic_conversion[message.topic], new_document)


if __name__ == '__main__':
    PreprocessorService().get_service()






