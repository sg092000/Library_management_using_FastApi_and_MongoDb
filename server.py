from fastapi import FastAPI
from models import Book
from config import get_books 

app = FastAPI()

@app.get("/books/", response_model=list[Book])
def get_all_books():
    return get_books()
