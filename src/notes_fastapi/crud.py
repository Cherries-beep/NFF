"""модуль для операций с БД через SQLAlchemy"""
from sqlalchemy.orm import Session
from models import Note

def get_note(db: Session, note_id: int):

    return db.query(Note).filter(Note.id == note_id).first()

def get_notes(db: Session, skip:  int = 0,  limit: int = 100):

    return db.query(Note).offset(skip).limit(limit).all()

def create_note(db: Session, title: str, content: str):
    db_note = Note(title=title, content=content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

def update_note(db: Session, note_id: int, title: str = None, content: str = None):
    db_note = get_note(db=db, note_id=note_id)

    if not note_id:
        return None

    if title:
        db_note.title = title

    if content:
        db_note.content = content

    db.commit()
    db.refresh(db_note)

    return db_note

def delete_note(db: Session, note_id: int):
    db_note = get_note(db=db, note_id=note_id)

    if not db_note:
        return None

    db.delete(db_note)
    db.commit()

    return db_note






