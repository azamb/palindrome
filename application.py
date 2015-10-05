#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''application.py

Usage:
    application.py [--port=<port>] [--host=<host>] [--debug]

Options:
    -h, --help          Show this message and quit.
    --port=<port>       Specify the port to bind to.
                    [default: 8080]
    --host=<host>       Specify the host to bind to.
                    [default: localhost]
    --debug             Enable debugging.
'''
from docopt import docopt
from flask import Flask
from api import create_api


if __name__ == '__main__':
    args = docopt(__doc__)
    port = int(args['--port'])
    host = args['--host']

    application = Flask(__name__)
    create_api(application)
    application.debug = args['--debug']

    application.run(host=host, port=port)
