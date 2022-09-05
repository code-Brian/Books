from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
        WHERE authors.id = %(id)s
        '''

        # store the query in a result variable
        result = connectToMySQL('books').query_db(query, data)

        # return the result at the first index of the list within the instance of the class
        return cls(result[0])


