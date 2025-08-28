from pymongo import ASCENDING

from app.core import Database


class TweetsDal:
    def __init__(self, db: Database):
        """Constructor."""
        # self.collection = None
        self.db = db

    # def open_connection(self, collection):
    #     """Open a database connection."""
    #     self.collection = self.db.get_db_collection(collection)
    #     return collection

    async def list(self, collection_name):
        """List all tweets in the database."""
        return await self.db.get_db_collection(collection_name).find().to_list()

    async def list_skip_limit(self,collection_name, skip_num, limit_num) -> list:
        """List tweets in the database with skip and limit."""
        return await (self.db.get_db_collection(collection_name).find()
                      .sort([("CreateDate", ASCENDING), ("_id", ASCENDING)])
                      .skip(skip_num)
                      .limit(limit_num)
                      .to_list())

    async def insert_document(self, collection_name, document):
        result = await self.db.get_db_collection(collection_name).insert_one(document)
        document['tweet_id'] = str(result.inserted_id)
        return document

