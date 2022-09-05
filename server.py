from flask_app import app

# flask_app controller imports
from flask_app.controllers import authors
from flask_app.controllers import books

if __name__ == '__main__':
    app.run(debug=True)