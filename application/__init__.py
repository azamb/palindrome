from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from api import create_api

application = Flask(__name__)
create_api(application)
application.config.from_object('config')
db = SQLAlchemy(application)
