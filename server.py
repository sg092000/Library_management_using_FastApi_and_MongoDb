from fastapi import FastAPI
from models import Book
from config import get_books , create_book , get_book

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

@app.post("/books/", response_model=Book)
def create_new_book(book: Book):
    try:
        return create_book(book)
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the create_new_book method",
            "Error" : e.args[0]
        }
        raise e
        return df
        
@app.get("/books/{book_id}", response_model=Book)
def get_single_book(book_id: str):
    try:
        book = get_book(book_id)
        if book:
            return book
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_single_book method",
            "Error" : e.args[0]
        }
        raise e
        return df