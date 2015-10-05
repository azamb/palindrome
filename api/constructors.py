from flask.ext import restful
from api.resources import MessageResource, MessageListResource


NAME = 'pal'
VERSION = 1


def create_api(app):
    '''
        Creates the Palindrome api along with its routes.

        :param app: The Flask app that the api registers with
        :type app: flask.app.Flask

        :returns: The palindrome API
        :rtype: flask_restful.Api
    '''
    api_prefix = '/{0}/v{1}'.format(NAME, VERSION)
    api = restful.Api(app, prefix=api_prefix)

    api.add_resource(MessageListResource, '/messages')
    api.add_resource(
        MessageResource,
        '/messages/<message_id>',
        endpoint='messages'
    )

    return api
