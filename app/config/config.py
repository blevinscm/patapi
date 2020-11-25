from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    uri: db_server = os.environ['MONGO_URL']


settings = Settings()