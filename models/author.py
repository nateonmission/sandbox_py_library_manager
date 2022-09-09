import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from db_setup import Base
from .mixins import Timestamp


class Author(Timestamp, Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=False, index=True, nullable=True)
    author = Column(String(100), unique=False, index=False, nullable=True)
    date_of_birth = Column(Date, unique=False, index=False, nullable=True)
    date_of_death = Column(Date, unique=False, index=False, nullable=True)
    is_active = Column(Boolean, default=True)
    description = Column(Text, unique=False, index=False, nullable=True)
    img_link = Column(String(100), unique=False, index=False, nullable=True)


    # profile = relationship("Profile", back_populates="owner", uselist=False)
    # student_courses = relationship("StudentCourse", back_populates="student")
    # student_content_blocks = relationship("CompletedContentBlock", back_populates="student")

