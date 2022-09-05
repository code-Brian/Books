from flask_app import app
# flask_app controller imports
from flask_app.controllers import authors, books

if __name__ == '__main__':
    app.run(debug=True)