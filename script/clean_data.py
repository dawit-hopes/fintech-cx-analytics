import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

def ensure_nltk_resources():
    """Download required NLTK resources if they are missing."""
    resources = {
        "stopwords": "corpora/stopwords",
        "wordnet": "corpora/wordnet",
        "omw-1.4": "corpora/omw-1.4",
    }

    for resource, path in resources.items():
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(resource)

class DataCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words.update(['app', 'bank', 'mobile', 'android', 'phone', 'service', 'account'])
        ensure_nltk_resources()

    def clean_text(self, text:str)-> str:
        """
        Cleans the data not to include html
        """

        if not isinstance(text, str):
         return ""

        text = re.sub(r'https?://\S+|www\.\S+|<html>.*?</html>|<.*?>', '', text)
        text = re.sub(r'[^a-z\s]', '', text)

        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(word) for  word in tokens if word not in self.stop_words]

        return " ".join(tokens)
       