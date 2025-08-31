from time import sleep

from app.services.retriever import RetrieverService


class RetrieverManager:
    def __init__(self):
        self.retriever_service = RetrieverService()

    async def retrieve(self):
        skip = 0
        limit = 100
        while True:
            tweets = await self.retriever_service.retrieve_tweets(skip=skip, limit=limit)
            self.retriever_service.publish_tweets(tweets)
            skip += len(tweets)
            sleep(60)
