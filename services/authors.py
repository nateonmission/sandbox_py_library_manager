from sqlalchemy.orm import Session

from models.author import Author
from pydantic_schemas.authors import AuthorCreate


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Author).offset(skip).limit(limit).all()

def get_author_by_id(db: Session, id: int):
    return db.query(Author).filter(Author.id == id).first()

def get_author_by_name(db: Session, name: str):
    author = db.query(Author).filter(Author.name == name).first()
    return author

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author