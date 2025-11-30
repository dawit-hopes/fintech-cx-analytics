from google_play_scraper import reviews_all, Sort
import pandas as pd

class Scraper:
    def __init__(self):
        self.BANK_APPS = {
            "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
            "Bank of Abyssinia": "com.boa.boaMobileBanking",
            "Dashen Bank": "com.dashen.dashensuperapp"
        }
        
    def scrape_bank_reviews(self, app_id:str, app_name:str)-> pd.DataFrame:
        '''
        Scrape all reviews for a given bank app from Google Play Store.
        Parameters:
            app_id (str): The unique identifier of the app on Google Play Store.
            app_name (str): The name of the bank app.
        Returns:
            pd.DataFrame: A DataFrame containing all reviews for the specified app.
        '''
        
        result:list[dict] = reviews_all(
            app_id,
            sleep_milliseconds=0,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
        )
        
        df = pd.DataFrame(result)
        df['app_name'] = app_name
                
        df = df[['app_name', 'content', 'score', 'at']]
        df.rename(columns={'content': 'review', 'at': 'date', "app_name": "bank", "score": "rating"}, inplace=True)
        df['date'] = pd.to_datetime(df['date']).dt.date
        
        return df
        
        