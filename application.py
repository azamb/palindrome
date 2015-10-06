#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from api import create_api
from constants import PALINDROME_DB_URI, SECRET_KEY


application = Flask(__name__)
create_api(application)


@application.before_first_request
def config_app():
    if not application.config.get('INITIALIZED'):
        # TODO remove debug statement.
        application.config['DEBUG'] = True
        application.config['SECRET_KEY'] = SECRET_KEY
        application.config['SQLALCHEMY_DATABASE_URI'] = PALINDROME_DB_URI
        application.config['INITIALIZED'] = True


if __name__ == '__main__':
    application.run()
