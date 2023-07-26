from pymongo import MongoClient
from models import Book

client = MongoClient('mongodb://localhost:27017')
db = client['library_db']
books_collection = db['books']

def get_books():
    return list(books_collection.find())
