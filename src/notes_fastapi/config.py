""" Единая точка, откуда приложение читает DATABASE_URL """
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = '.env'

settings = Settings()