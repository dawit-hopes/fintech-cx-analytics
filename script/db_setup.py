from sqlalchemy import create_engine
from src.models import Base

engine = create_engine("postgresql://postgres:postgres@localhost:5432/bank_reviews")
Base.metadata.create_all(engine)    

