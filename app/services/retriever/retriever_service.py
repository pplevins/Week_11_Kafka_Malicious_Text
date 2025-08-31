from core import Database
from dal import TweetsDal
from models import Producer


class RetrieverService:
    def __init__(self):
        self._producer = Producer()
        self._dal = TweetsDal(Database())

    async def retrieve_tweets(self, skip, limit):
        tweets = await self._dal.list_skip_limit('tweets', skip, limit)
        return tweets

    def publish_tweets(self, tweets):
        for tweet in tweets:
            massage = {
                "source_id": tweet["_id"],
                "create_date": tweet["CreateDate"],
                "text": tweet["text"],
                "antisemitic": tweet["Antisemitic"]
            }
            topic = "raw_tweets_antisemitic" if tweet["Antisemitic"] \
                else "raw_tweets_not_antisemitic"
            self._producer.publish_massage(topic, massage)
