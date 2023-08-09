from fastapi import FastAPI , HTTPException
from models import Book, User
from fastapi.openapi.docs import get_swagger_ui_html
from config import get_books, create_book, get_book, update_book, delete_book , create_user , get_users , get_user , add_book_to_user

app = FastAPI()

@app.get("/docs")
def read_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json")

@app.get("/books/", response_model=list[Book])
def get_all_books():
    try:
        return get_books()
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_all_books method",
            "Error" : e
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
            "Error" : e
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
            "Error" : e
        }
        raise e
        return df

@app.put("/books/{book_id}", response_model=Book)
def update_existing_book(book_id: str, book: Book):
    try:
        updated_book = update_book(book_id, book)
        if updated_book.modified_count == 1:
            return book
        else:
            return {"message": "Book not found"}
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the update_existing_book method",
            "Error" : e
        }
        raise e
        return df

@app.delete("/books/{book_id}")
def delete_existing_book(book_id: str):
    try:
        book = delete_book(book_id)
        return book
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the delete_existing_book method",
            "Error" : e
        }
        raise e
        return df
    
@app.post("/users/", response_model=User)
def create_new_user(user: User):
    try:
        return create_user(user)
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the create_new_user method",
            "Error" : e
        }
        raise e
        return df

@app.get("/users/", response_model=list[User])
def get_all_users():
    try:
        return get_users()
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_all_users method",
            "Error" : e
        }
        raise e
        return df

@app.get("/users/{user_id}", response_model=User)
def get_single_user(user_id: str):
    try:
        user = get_user(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_single_user method",
            "Error" : e
        }
        raise e
        return df

@app.put("/users/{user_id}/add_book/{book_id}", response_model=User)
def add_book_to_user_endpoint(user_id: str, book_id: str):
    try:
        if add_book_to_user(user_id, book_id):
            return get_user(user_id)
        else:
            raise HTTPException(status_code=404, detail="Book or User not found")
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the add_book_to_user_endpoint method",
            "Error" : e
        }
        raise e
        return df