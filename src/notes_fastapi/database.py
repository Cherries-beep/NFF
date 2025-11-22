"""модуль для подключения к PostgreSQL и session maker"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:password@localhost:5432/notes_db"

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    """ Возвращает сессию бд. Создает объект SessionLocal, отдает его в виде генератора и закрывает соединение
    после завершения запроса

    :returns: сессия  sqlAlchemy для операций с бд
    :rtype: Session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()