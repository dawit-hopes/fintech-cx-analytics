from transformers import pipeline
import pandas as pd

SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline("sentiment-analysis", model=SENTIMENT_MODEL)


class SentimentAnalysis:
    def __init__(self):
        self.classifier = classifier


    def run_sentiment_analysis(self, text: str) -> (str, float):
        """
        Run sentiment analysis on the given text

        Args:
            text (str): The text to run sentiment analysis on

        Returns:
            (str, float): The sentiment label and score
        """

        if not text or not isinstance(text, str):
            return 'NEUTRAL', 0.0

        try:

            result = self.classifier(text,  truncation=True, max_length=512)
            score = result[0]['score']
            label = result[0]['label']
            
            if 0.45 < score < 0.55:
                return 'NEUTRAL', score
            
            return label, score

        except Exception as e:
            print(f"Error running sentiment analysis: {e}")
            return 'ERROR', 0.0