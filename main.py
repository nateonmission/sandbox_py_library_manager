from fastapi import FastAPI

from routes import books, authors
from db_setup import engine
from models import book, author

book.Base.metadata.create_all(bind=engine)
author.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Fast API LMS",
    description="Library Management System.",
    version="0.0.1",
    contact={
        "name": "Nate",
        "email": "nate@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(books.router)
app.include_router(authors.router)
