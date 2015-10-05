from flask.ext.restful import Resource, reqparse
from db.external import (
    connection,
    get_messages,
    get_message,
    add_message,
    delete_message
)
from db import helpers


class MessageResource(Resource):
    def get(self, message_id):
        '''
            Get a single message
        '''
        with connection() as session:
            message = get_message(session, message_id)
            return message.to_dict()

    def delete(self, message_id):
        '''
            Delete a single message
        '''
        with connection() as session:
            message = delete_message(session, message_id)
            return message.to_dict()


class MessageListResource(Resource):
    def get(self):
        '''
            List all messages.
        '''
        with connection() as session:
            messages = get_messages(session)
            messages = [msg.to_dict() for msg in messages]

            return {'messages': messages}

    def post(self):
        '''
            Add a new message
        '''
        rp = reqparse.RequestParser()
        rp.add_argument('message', type=unicode, required=True)
        rp.add_argument('username', type=unicode, required=True)
        args = rp.parse_args()

        message = args['message']
        username = args['username']
        is_palindrome = helpers.is_palindrome(message)

        with connection() as session:
            msg = add_message(session, message, username, is_palindrome)
            return msg.to_dict()

__all__ = ['MessageResource', 'MessageListResource']
