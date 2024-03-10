from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo.mongo_client import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


# MongoDB setup
uri = "mongodb+srv://admin:admin@cluster0.vgkg7px.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['your_database_name']  # Explicitly specify your database name here
libdata = db.bookData

liata = ["GameOfThrones", "Harry Potter", "Dune"]


# # Iterate over the list and insert each item into the libdata collection
# for title in liata:
#     libdata.insert_one({"title": title,"URL":"www.google.com"})

# print("Books have been stored in the database.")
books_list = []
for book in libdata.find():
    books_list.append(book)

print(books_list)