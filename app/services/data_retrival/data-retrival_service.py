from app.core import Database
from app.dal import TweetsDal


class DataRetrivalService:
    def __init__(self):
        self.dal = TweetsDal(Database())

    def antisemitic_retriv(self):
        return self.dal.list('antisemitic')

    def non_antisemitic_retriv(self):
        return self.dal.list('non_antisemitic')