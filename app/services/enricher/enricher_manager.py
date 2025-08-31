from utils import TextAnalyzer


class EnricherManager:
    def __init__(self, document):
        self.analyzer = TextAnalyzer()
        self.document = document
        self.clean_text = document['clean_text']

    def process(self):
        self.document['sentiment'] = self.analyzer.calculate_text_sentiment(self.clean_text)
        self.document['weapon_detected'] = self.analyzer.find_weapons(self.clean_text)
        self.document['relevant_timestamp'] = self.analyzer.find_latest_date(self.document['text'])

        return self.document

    def get_document(self):
        self.process()
        return self.document
