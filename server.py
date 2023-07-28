from fastapi import FastAPI
from models import Book
from config import get_books , create_book

app = FastAPI()

@app.get("/books/", response_model=list[Book])
def get_all_books():
    try:
        return get_books()
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_all_books method",
            "Error" : e.args[0]
        }
        raise e
        return df

