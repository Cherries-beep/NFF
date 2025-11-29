"""модуль для подключения к PostgreSQL и session maker"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

DATABASE_URL = "postgresql://postgres:password@localhost:5432/notes_db" # урл для приложения фастапи

engine = create_engine( # create_engine - создание подключения к бд. Движок
    url=DATABASE_URL,
    echo=True # вывод SQL запросов в консоль
)

SessionLocal = sessionmaker( # фабрика сессий
    autocommit=False, # не коммитить SQL запрос сразу в базу
    autoflush=False, # отправка изменений в бд без коммита
    bind=engine # связка к определенной бд
)

Base = declarative_base() # основа, базовый класс для всех sqlalchemy моделей