from pymongo import MongoClient
from models import Book

client = MongoClient('mongodb://localhost:27017')
db = client['library_db']
books_collection = db['books']

def get_books():
    try:
        return list(books_collection.find())
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_books method",
            "Error" : e.args[0]
        }
        raise e
        return df

def create_book(book: Book):
    try:
        books_collection.insert_one(book.dict())
        return book
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the create_book method",
            "Error" : e.args[0]
        }
        raise e
        return df