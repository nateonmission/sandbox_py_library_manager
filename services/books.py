from sqlalchemy.orm import Session

from models.book import Book
from pydantic_schemas.books import BookCreate
from .authors import get_author_by_id, get_author_by_name

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

def get_book_by_id(db: Session, id: int):
    return db.query(Book).filter(Book.id == id).first()

def create_book(db: Session, book: BookCreate):

    ids = []
    for author in book.author_id:
        try:
            author_model = get_author_by_name(db, author)
        except:
            pass

        ids.append(author_model.id)
    db_book = Book(
        title=book.title,
        author_id = ids
        )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book