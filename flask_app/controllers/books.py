from flask import Flask, render_template, redirect, request, session
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app

@app.route('/books')
def books():
    print('going to books page')
    
    return render_template('books.html', books=Book.get_all())

@app.route('/books/show')
def books_show():
    print('going to individual book page at books.id')
    return render_template('books_show.html')