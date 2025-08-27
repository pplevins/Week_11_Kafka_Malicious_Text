from app.core import Database
from app.dal import TweetsDal
from app.models import Producer


class RetrieverService:
    def __init__(self):
        self._producer = Producer()
        self._dal = TweetsDal(Database())

    async def retrieve_tweets(self, skip, limit):
        self._dal.open_connection("tweets")
        tweets = await self._dal.list_skip_limit(skip, limit)
        return tweets

    def publish_tweets(self, tweets):
        for tweet in tweets:
            massage = {
                "id": str(tweet["_id"]),
                "CreateDate": tweet["CreateDate"],
                "original_text": tweet["text"],
                "Antisemitic": tweet["Antisemitic"]
            }
            topic = "raw_tweets_antisemitic" if tweet["Antisemitic"] \
                else "raw_tweets_not_antisemitic"
            self._producer.publish_massage(topic, massage)
