import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI =  f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_URL")}/{os.getenv("DB_NAME")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = 1