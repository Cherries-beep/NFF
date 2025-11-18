"""SQLAlchemy модели"""
from sqlalchemy import Column, Integer, String
from database import Base

class Note(Base):
    __tablename__ = 'notes'

    id = Column(type_=Integer, primary_key=True, index=True)
    title = Column(type_=String, index=True)
    content = Column(type_=String)