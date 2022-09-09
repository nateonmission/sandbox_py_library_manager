import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Date, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from db_setup import Base
from .mixins import Timestamp


class Genre(enum.Enum):
    FICTION_SciFi = 1
    FICTION_YA = 2
    FICTION_Historical = 3
    NONFICTION_Coding = 4
    NONFICTION_Support = 5
    NONFICTION_Security = 6
    NONFICTION_Religion = 7
    LANGUAGE_French = 8
    LANGUAGE_German = 9
    LANGUAGE_Spanish = 10
    LANGUAGE_Portuguese = 11
    LANGUAGE_Italian = 12
    LANGUAGE_Classics = 13


class Book(Timestamp, Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, index=True, nullable=False)
    author_id = Column(ARRAY(Integer),  nullable=True)
    genre = Column(Enum(Genre))
    is_active = Column(Boolean, default=True)
    publisher: Column(String(100), unique=False, index=False, nullable=True)
    isbn_10 = Column(String(20), unique=False, index=False, nullable=True)
    isbn_13 = Column(String(20), unique=False, index=False, nullable=True)
    description = Column(Text, unique=False, index=False, nullable=True)
    date_published = Column(Date, unique=False, index=False, nullable=True)
    amzn_link = Column(String(100), unique=False, index=False, nullable=True)
    img_link = Column(String(100), unique=False, index=False, nullable=True)


    # profile = relationship("Profile", back_populates="owner", uselist=False)
    # student_courses = relationship("StudentCourse", back_populates="student")
    # student_content_blocks = relationship("CompletedContentBlock", back_populates="student")

