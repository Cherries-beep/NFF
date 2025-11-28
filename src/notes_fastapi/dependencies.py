""" Модуль с dependency injection """

from src.notes_fastapi.database import SessionLocal
from typing import Generator

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()