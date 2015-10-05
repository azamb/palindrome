class MessageNotFound(Exception):
    msg = 'Mesage with id: {0} not found'

    def __init__(self, id):
        return super(MessageNotFound, self).__init__(self.msg.format(id))
