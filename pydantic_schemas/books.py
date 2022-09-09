from  typing import List
from pydantic import BaseModel
from pydantic.schema import Optional
from datetime import datetime
from enum import Enum


class BookBase(BaseModel):
    title: str


class BookCreate(BookBase):
    author_id: Optional[list[str]]
    genre: Optional[str]
    publisher: Optional[str]
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]
    date_published: Optional[datetime]
    amzn_link: Optional[str]
    img_link: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class Book(BookBase):
    id: int
    author_id: Optional[list[int]]
    genre: Optional[str]
    publisher: Optional[str]
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]
    date_published: Optional[datetime]
    amzn_link: Optional[str]
    img_link: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]



    class Config:
        orm_mode = True