from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    title: str
    description: str
    price: int
    author: str
    published_year: int

class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    email_id: str
    contact: str
    books: List[Book] = []
