from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db_setup import get_db
from pydantic_schemas.books import BookCreate, Book
from services.books import get_book_by_id, get_books, create_book

router = fastapi.APIRouter()


@router.get("/books", response_model=List[Book])
async def api_get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = get_books(db, skip=skip, limit=limit)
    return books

@router.post("/books")
async def api_create_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book)

@router.get("/books/{id}", response_model=Book)
async def api_get_book( id: int, db: Session = Depends(get_db)):
    return get_book_by_id(db=db, user_id=id)