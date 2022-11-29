from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#imports must be done after the app initiation
from Controllers import ResetController
from Controllers.EventController import Event
from Controllers.AccountController import AccountController
from Models import Account
