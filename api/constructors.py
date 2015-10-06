from flask.ext import restful
from api.resources import MessageResource, MessageListResource
from error_handler import api_error_handler

VERSION = 1


def create_api(app):
    '''
        Creates the Palindrome api along with its routes.

        :param app: The Flask app that the api registers with
        :type app: flask.app.Flask

        :returns: The palindrome API
        :rtype: flask_restful.Api
    '''
    api = restful.Api(app, prefix='/v{0}'.format(VERSION))
    api.decorators = [api_error_handler]
    api.add_resource(MessageListResource, '/messages')
    api.add_resource(
        MessageResource,
        '/messages/<message_id>',
        endpoint='messages'
    )

    return api
