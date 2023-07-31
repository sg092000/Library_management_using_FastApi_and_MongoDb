from pymongo import MongoClient
from models import Book , User
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client['library_db']
books_collection = db['books']
users_collection = db['users']

def get_books():
    try:
        return list(books_collection.find())
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_books method",
            "Error" : e
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
            "Error" : e
        }
        raise e
        return df

def get_book(book_id: str):
    try:
        return books_collection.find_one({"_id": ObjectId(book_id)})
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_book method",
            "Error" : e
        }
        raise e
        return df

def update_book(book_id: str, book: Book):
    try:
        return books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": book.dict()})
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the update_book method",
            "Error" : e
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
            "Error" : e
        }
        raise e
        return df
    
def create_user(user: User):
    try:
        users_collection.insert_one(user.dict())
        return user
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the create_user method",
            "Error" : e
        }
        raise e
        return df

def get_users():
    try:
        return list(users_collection.find())
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_users method",
            "Error" : e
        }
        raise e
        return df

def get_user(user_id: str):
    try:
        return users_collection.find_one({"_id": ObjectId(user_id)})
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the get_user method",
            "Error" : e
        }
        raise e
        return df

def add_book_to_user(user_id: str, book_id: str):
    try:
        user = get_user(user_id)
        my_book = get_book(book_id)
        if user and my_book not in [book for book in user['books']]:
            if my_book:
                users_collection.update_one({"_id": ObjectId(user_id)}, {"$push": {"books": my_book}})
                return True
        
        return False
    except Exception as e:
        df = {
            "Error_Message": "Something went wrong in the add_book_to_user method",
            "Error" : e
        }
        raise e
        return df