from app.models import Consumer


class PersisterService:
    def __init__(self):
        self.topics = ('enriched_preprocessed_tweets_antisemitic','enriched_preprocessed_tweets_not_antisemitic')
        self.topic_conversion = {self.topics[0]:'tweets_antisemitic', self.topics[1]:'tweets_not_antisemitic'}
        self.consumer = Consumer(self.topics)



