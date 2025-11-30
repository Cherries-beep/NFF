"""модуль для подключения к PostgreSQL и session maker"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings # settings уже берет переменные из .env


# create_engine - создание подключения к бд. Движок
# echo=True вывод SQL запросов в консоль
engine = create_engine(url=settings.DATABASE_URL, echo=True)

SessionLocal = sessionmaker( # фабрика сессий
    autocommit=False, # не коммитить SQL запрос сразу в базу
    autoflush=False, # отправка изменений в бд без коммита
    bind=engine # связка к определенной бд
)

Base = declarative_base() # основа, базовый класс для всех sqlalchemy моделей