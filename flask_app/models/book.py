from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_favorited = []

    # create a class method to retrieve all books from the database
    @classmethod
    def get_all(cls):
        # define the SQL query which selects all books from the database
        query = '''
        SELECT * FROM books;
        '''

        # store the results in a variable
        results = connectToMySQL('books').query_db(query)
        # create a list to store the instances of each book in, once we iterate over them
        books = []

        # iterate over the query results and append them to the books list
        for book in results:
            # each book gets appended by getting created as an instance via the cls method
            books.append(cls(book))
        # return the list of results
        return books

    # this class method is used to query the database and retrieve one book based on the book id passed in
    @classmethod
    def get_one(cls, data):
        # store the query which gets passed into the database
        query = '''SELECT * FROM books
        WHERE id = %(id)s
        '''

        # store the result so we can reference the first index of the returned list
        result = connectToMySQL('books').query_db(query,data)

        # return the result of my query at the first index of the returned list
        return cls(result[0])

    @classmethod
    def add_book_to_favorites(cls, data):
        # create an initial query and store it in a variable 
        query = '''
        INSERT INTO favorites (author_id, book_id)
        VALUES (%(author_id)s, %(book_id)s)
        '''

        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def get_book_favorites(cls, data):
        # store the SQL query in a variable
        query = '''SELECT * FROM favorites
        JOIN books ON books.id = book_id
        LEFT JOIN authors ON authors.id = author_id
        WHERE book_id = %(id)s;
        '''

        # store the results of the query in a variable
        results = connectToMySQL('books').query_db(query, data)

        print(f'{results} BOOKS WITH AUTHORS WHO FAVORITED THEM --------------------------------------------------------------')

        if len(results) != 0:
            favorites = cls(results[0])

            # iterate over the results and store relevant data to be passed into each new instance of author
            for row in results:
                author_data = {
                    'id' : row.get('author_id'),
                    'name' : row.get('name')
                }
            



