from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/authors')
def r_authors():
    print('going to authors home page')
    return render_template('authors.html', authors=Author.get_all())

# this is for the form to create a new author and redirect back to the authors page
@app.route('/author/create', methods=['POST'])
def f_author_create():

    # incoming form data using request.form.get(<matching fields go here>)
    data = {
        'name': request.form.get('new_author')
    }

    print('creating a new author...')

    # pass the prepared statement into the author model and process the query specified by the incoming form data
    Author.create(data)

    return redirect('/authors')


# this will eventually get changed to pass in the author.id from the database, and redirect to the particular author.
@app.route('/authors/<int:id>/show')
def authors_show(id):

    # capture author id from route, and pass it to the database query to get the author information by the author id passed in
    data = {
        'id': id
    }

    # pass data captured into database query
    author = Author.get_one(data)

    # pass data captured into database query for author favorites
    favorites = Author.get_author_favorites(data)

    print('going to author page at authors.id...')

    return render_template('authors_show.html', author=author, favorites=favorites)