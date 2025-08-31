from utils.text_cleaner import TextCleaner


class PreprocessorManager:
    def __init__(self, text):
        self._text = text
        self._text_cleaner = TextCleaner()

    def process(self):
        removed_punctuation = self._text_cleaner.clean_punctuation(self._text)
        lower_text = self._text_cleaner.lower_text(removed_punctuation)
        removed_whitespaces = self._text_cleaner.remove_duplicate_whitespaces(lower_text)
        lemmatized_text = self._text_cleaner.lemmatize(removed_whitespaces)
        removed_stopwords = self._text_cleaner.remove_stopwords(lemmatized_text)
        return removed_stopwords
