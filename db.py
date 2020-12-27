import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from models import Reader
from models import Author
from models import Book

load_dotenv()

Base = declarative_base()
engine = create_engine(
    f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_URL")}/{os.getenv("DB_NAME")}')
session = sessionmaker(bind=engine)()


def recreate_database():
    print('Recreating database...')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
