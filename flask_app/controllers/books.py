from flask import Flask, render_template, redirect, request, session
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app

@app.route('/books')
def books():
    print('going to books page')
    
    return render_template('books.html', books=Book.get_all())

@app.route('/books/<int:id>/show')
def books_show(id):
    print('going to individual book page at books.id')

    # capture the incoming book id in a data dictionary
    data = {
        'id' : id
    }

    return render_template('books_show.html', book=Book.get_one(data), authors=Author.get_all())