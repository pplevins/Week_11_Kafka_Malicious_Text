from time import sleep

from app.services.retriever import RetrieverService


class RetrieverManager:
    def __init__(self):
        self.producer_service = RetrieverService()

    async def retrieve(self):
        skip = 0
        limit = 100
        while True:
            tweets = await self.producer_service.retrieve_tweets(skip=skip, limit=limit)
            self.producer_service.publish_tweets(tweets)
            skip += limit
            sleep(10)
