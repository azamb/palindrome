class MessageNotFound(Exception):
    msg = 'Message with id: {0} was not found'

    def __init__(self, id):
        return super(MessageNotFound, self).__init__(self.msg.format(id))
