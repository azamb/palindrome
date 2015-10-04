from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)

    # def __init__(self, notes):
    #     self.notes = notes

    # def __repr__(self):
    #     return '<Data %r>' % self.notes
