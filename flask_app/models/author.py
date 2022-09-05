from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_favorites = []

    # define a class method which queries the database and returns all authors in the authors table
    @classmethod
    def get_all(cls):
        # create the query to pass into SQL database
        query = '''
        SELECT * FROM authors;
        '''
        # pass the query into our database, and store it in a results variable
        results = connectToMySQL('books').query_db(query)

        # create an empty list of authors
        authors = []

        # iterate over the results returned by the query
        for author in results:
            authors.append(cls(author))

        # return the list of authors after iterating
        return authors

    # define a class method which queries the database and returns the author id specified in the authors table
    @classmethod
    def get_one(cls, data):
        # create a query for our database, and pass in the id specified
        query = '''
        SELECT * FROM authors
        WHERE authors.id = %(id)s;
        '''

        # store the query in a result variable
        result = connectToMySQL('books').query_db(query, data)

        # return the result at the first index of the list within the instance of the class
        return cls(result[0])

    # define a class method which queries the database to insert a new author into the authors table
    @classmethod
    def create(cls, data):
        # create a query which passes in form data and creates a new author in the authors table
        query = '''
        INSERT INTO authors (name, created_at, updated_at)
        VALUES (%(name)s, NOW(), NOW() );
        '''
        # return with the connectToMySQL statement with the query being passed into the database
        return connectToMySQL('books').query_db(query, data)

    # create a class method which joins authors and books info together via the favorites table foreign keys
    # this will return with the name of the author, book title, and book pages
    @classmethod
    def get_author_favorites(cls,data):

        # this query is used to return the favorited books by the author
        query ='''SELECT * FROM favorites
        JOIN authors ON authors.id = author_id
        LEFT JOIN books ON books.id = book_id
        WHERE author_id = %(id)s;
        '''

        # store the result in a variable so you can reference the first index of the list
        results = connectToMySQL('books').query_db(query,data)

        # store the Author object in a variable so you can access the attributes and iterate over them
        favorite = cls(results[0])

        # iterate over the results and store each row in a book_data dictionary
        for row in results:
            book_data = {
                'id': row.get('books.id'),
                'title' : row.get('title'),
                'num_pages' : row.get('num_pages'),
                'created_at' : row.get('books.created_at'),
                'updated_at' : row.get('books.updated_at')
            }

            # the book_data will be passed into an instance of a book class on each iteration, and will be appended to the authors favorites list
            favorite.author_favorites.append(book.Book(book_data))

        # return the instance of the author object at the end of the loop
        return favorite

