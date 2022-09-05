from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.author import Author

@app.route('/authors')
def authors():
    print('going to authors home page')
    authors=Author.get_all()
    return render_template('authors.html', authors=authors)

# this will eventually get changed to pass in the author.id from the database, and redirect to the particular author.
@app.route('/authors/show')
def authors_show():
    print('going to author page at authors.id...')
    return render_template('authors_show.html')