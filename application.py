#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from api import create_api
from constants import PALINDROME_DB_URI, SECRET_KEY


application = Flask(__name__)
create_api(application)


@application.before_first_request
def config_app():
    if not application.config.get('INITIALIZED'):
        application.config['SECRET_KEY'] = SECRET_KEY
        application.config['SQLALCHEMY_DATABASE_URI'] = PALINDROME_DB_URI
        application.config['INITIALIZED'] = True


@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # TODO remove debug statement.
    application.debug = True
    application.run()
