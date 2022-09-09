from pydantic import BaseModel
from pydantic.schema import Optional
from datetime import datetime
from enum import Enum

class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    ...


class Author(AuthorBase):
    id: int
    name: str
    date_of_birth: Optional[datetime]
    date_of_death: Optional[datetime]
    description: Optional[str]
    is_active: Optional[str]
    img_link: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True