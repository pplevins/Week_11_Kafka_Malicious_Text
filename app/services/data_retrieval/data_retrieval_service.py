from core import Database
from dal import TweetsDal


class DataRetrievalService:
    def __init__(self):
        self.dal = TweetsDal(Database())

    async def retrieve_antisemitic(self):
        tweets = await self.dal.list('tweets_antisemitic')
        for tweet in tweets:
            tweet['_id'] = str(tweet['_id'])
        return tweets

    async def retrieve_non_antisemitic(self):
        tweets = await self.dal.list('tweets_not_antisemitic')
        for tweet in tweets:
            tweet['_id'] = str(tweet['_id'])
        return tweets
