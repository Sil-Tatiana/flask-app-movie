from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviesDB.db'
app.config['SECRET_KEY'] = 'secret'

# Create the database object, which is an instance of the SQLAlchem
db = SQLAlchemy(app)

from applications import routes