import os
import re
import string

import nltk
from nltk import word_tokenize, WordNetLemmatizer, pos_tag
from nltk.corpus import stopwords


class TextCleaner:
    """A utility class to clean up text and preprocess it."""

    def __init__(self):
        nltk_dir = "/tmp/nltk_data"
        os.makedirs(nltk_dir, exist_ok=True)
        nltk.data.path.append(nltk_dir)
        nltk.download('stopwords', download_dir=nltk_dir, quiet=True)
        nltk.download('punkt', download_dir=nltk_dir, quiet=True)
        nltk.download('punkt_tab', download_dir=nltk_dir, quiet=True)
        nltk.download('wordnet', download_dir=nltk_dir, quiet=True)
        nltk.download('omw-1.4', download_dir=nltk_dir, quiet=True)
        nltk.download('averaged_perceptron_tagger_eng', download_dir=nltk_dir, quiet=True)

    def lower_text(self, text):
        """Lowers text."""
        return text.lower()

    def clean_punctuation(self, text):
        """Cleans all punctuation and special characters."""
        return text.translate(str.maketrans('', '', string.punctuation))

    def remove_stopwords(self, text):
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text)
        return " ".join([word for word in tokens if word not in stop_words])

    def remove_duplicate_whitespaces(self, text):
        """Removes duplicate whitespaces."""
        return " ".join(re.split(r"\s+", text, flags=re.UNICODE)).strip()

    def lemmatize(self, text):
        """Lemmatizes text."""
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text)
        tagged_tokens = pos_tag(tokens)
        lemmatized_sentence = []
        for word, tag in tagged_tokens:
            if word.lower() == 'are' or word.lower() in ['is', 'am']:
                lemmatized_sentence.append(word)
            else:
                lemmatized_sentence.append(lemmatizer.lemmatize(word, self._get_wordnet_pos(tag)))

        return ' '.join(lemmatized_sentence)

    def _get_wordnet_pos(self, tag):
        """Inner function for getting wordnet pos tag for lemmatization."""
        if tag.startswith('J'):
            return 'a'
        elif tag.startswith('V'):
            return 'v'
        elif tag.startswith('N'):
            return 'n'
        elif tag.startswith('R'):
            return 'r'
        else:
            return 'n'
