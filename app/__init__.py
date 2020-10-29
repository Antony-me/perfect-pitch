from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']= 'stuxnet993.'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/perfectpitch'
db = SQLAlchemy(app)


from app import views