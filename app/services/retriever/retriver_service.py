from app.core import Database
from app.dal import TweetsDal
from app.models import Producer


class RetrieverService:
    def __init__(self):
        self._producer = Producer()
        self._dal = TweetsDal(Database())