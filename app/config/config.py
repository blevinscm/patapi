from pydantic import BaseSettings
import os

uri = os.environ['MONGO_URL']

class Settings(BaseSettings):
    uri: str 
    


settings = Settings()