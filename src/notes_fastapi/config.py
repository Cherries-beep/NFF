""" Единая точка, откуда приложение читает DATABASE_URL """
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = '.env'

settings = Settings