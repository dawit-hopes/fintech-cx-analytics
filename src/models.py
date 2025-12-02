from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Banks(Base):
    __tablename__ = "bank_reviews"
    bank_id = Column(Integer, primary_key=True)
    bank_name = Column(String)
    

class Reviews(Base):
    __tablename__ = "reviews"
    review_id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    bank_id = Column(Integer, ForeignKey("bank_reviews.bank_id"))
    review_text = Column(String)
    review_date = Column(Date)
    sentiment_label = Column(String)
    sentiment_score = Column(String)
    source = Column(String)