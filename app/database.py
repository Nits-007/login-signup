from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://autism_user:cEFS1vmtv9aZXjE2a5nLrCctJ5W4U5LP@dpg-cub8b6in91rc7391nn80-a/autism'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
