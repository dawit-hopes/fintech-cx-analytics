import pandas as pd
from sqlalchemy.orm import sessionmaker
from src.models import Reviews, Banks, Base
from sqlalchemy import create_engine

df = pd.read_csv("../data/reviews_dataset.csv")
df = df.rename(columns={'bank': 'bank_name'})


banks_df = df.drop_duplicates(['bank_name'])
banks_df['bank_id'] = banks_df.index + 1 
banks_data = banks_df.to_dict('records')


def insert_bank_data(engine, banks_data):
    """
    Insert bank data into the database.
    """

    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.bulk_insert_mappings(Banks, banks_data)
        session.commit()
        print(f"Inserted {len(banks_data)} banks into the database.")


def insert_review_data(engine, reviews_data):
    """
    Insert review data into the database.
    """

    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.bulk_insert_mappings(Reviews, reviews_data)
        session.commit()
        print(f"Inserted {len(reviews_data)} reviews into the database.")


def merge_data(df_one, banks_df):
    reviews_to_insert = pd.merge(
        df_one,
        banks_df[['bank_id', 'bank_name']],
        on='bank_name',
        how='inner'
    )

    reviews_to_insert = pd.drop_duplicates(reviews_to_insert, ['review'])
    reviews_to_insert['review_id'] = reviews_to_insert.index + 1 
    reviews_to_insert = reviews_to_insert.rename(columns={'review': 'review_text', "date": "review_date"})
    reviews_to_insert = reviews_to_insert[['review_id', 'bank_id', 'review_text', 'review_date', 'sentiment_label', 'sentiment_score', 'source', 'rating']]
    reviews_data = reviews_to_insert.to_dict('records')


    return reviews_data



if __name__ == "__main__":
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/bank_reviews")
    Base.metadata.create_all(engine)
    insert_bank_data(engine, banks_data)
    reviews_data = merge_data(df, banks_df)
    insert_review_data(engine, reviews_data)