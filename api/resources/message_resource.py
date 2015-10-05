from flask.ext.restful import Resource, marshal, reqparse, fields

from exceptions import MessageNotFound
from db.external import (
    connection,
    get_messages,
    get_message,
    add_message,
    delete_message
)
from db import helpers


class IsoDateTimeField(fields.Raw):
    def format(self, value):
        return value.isoformat()


message_fields = {
    'id': fields.Integer,
    'message': fields.String,
    'username': fields.String,
    'created_on': IsoDateTimeField,
    'is_palindrome': fields.Boolean
}


class MessageResource(Resource):
    def get(self, message_id):
        '''
            Get a single message
        '''
        with connection() as session:
            message = get_message(session, message_id)
            if message is None:
                raise MessageNotFound(message_id)
            return marshal(message, message_fields)

    def delete(self, message_id):
        '''
            Delete a single message
        '''
        with connection() as session:
            message = delete_message(session, message_id)

            if message is None:
                raise MessageNotFound(message_id)
            return marshal(message, message_fields)


class MessageListResource(Resource):
    def get(self):
        '''
            List all messages.
        '''
        with connection() as session:
            messages = get_messages(session)
            messages = [
                marshal(msg, message_fields) for msg in messages
            ]

            return messages

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
            msg = marshal(msg, message_fields)
            return msg
