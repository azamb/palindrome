from application import db


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, unique=False, nullable=False)
    username = db.Column(db.String(50), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.now())
    is_palindrome = db.Column(db.Boolean)

    def __init__(self, message, username, is_palindrome):
        self.message = message
        self.username = username
        self.is_palindrome = is_palindrome

    def __repr__(self):
        return '<User(message={0}, username={1})>'.format(
            self.message, self.username
        )
