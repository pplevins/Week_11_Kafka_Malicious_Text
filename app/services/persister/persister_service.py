from app.core import Database
from app.dal import TweetsDal
from app.models import Consumer



class PersisterService:
    def __init__(self):
        self.topics = ('enriched_preprocessed_tweets_antisemitic','enriched_preprocessed_tweets_not_antisemitic')
        self.topic_conversion = {self.topics[0]:'tweets_antisemitic', self.topics[1]:'tweets_not_antisemitic'}
        self.consumer = Consumer(self.topics)
        self.dal = TweetsDal(Database())

    def insert_to_db(self):

        for message in self.consumer.get_consumed_messages():
            self.dal.insert_document(self.topic_conversion[message.topic], message.value)


if __name__ == '__main__':
    PersisterService().insert_to_db()








