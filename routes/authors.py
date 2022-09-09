from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db_setup import get_db
from pydantic_schemas.authors import AuthorCreate, Author
from services.authors import get_author_by_id, get_authors, create_author

router = fastapi.APIRouter()


@router.get("/authors", response_model=List[Author])
async def api_get_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = get_authors(db, skip=skip, limit=limit)
    return authors

@router.post("/authors")
async def api_create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db=db, author=author)

@router.get("/authors/{id}", response_model=Author)
async def api_get_author( id: int, db: Session = Depends(get_db)):
    return get_author_by_id(db=db, user_id=id)