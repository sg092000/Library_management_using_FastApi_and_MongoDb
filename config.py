from pymongo import MongoClient
from models import Book
from bson import ObjectId

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

def get_book(book_id: str):
    try:
        return books_collection.find_one({"_id": ObjectId(book_id)})
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_book method",
            "Error" : e.args[0]
        }
        raise e
        return df

def update_book(book_id: str, book: Book):
    try:
        return books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": book.dict()})
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the update_book method",
            "Error" : e.args[0]
        }
        raise e
        return df

def delete_book(book_id: str):
    try:
        book = books_collection.delete_one({"_id": ObjectId(book_id)})
        return book
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the delete_book method",
            "Error" : e.args[0]
        }
        raise e
        return df
    