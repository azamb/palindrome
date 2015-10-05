from sqlalchemy.ext.declarative import declarative_base
from application import db

Base = declarative_base()


class Serialize(Base):
    __abstract__ = True

    def to_dict(self):
        return {
            k: v
            for k, v in self.__dict__.iteritems()
            if k != 'to_dict' and not k.startswith('_')
        }


class Messages(Serialize):
    # TODO docs
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, unique=False, nullable=False)
    username = db.Column(db.String(50), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.now())
    is_palindrome = db.Column(db.Boolean, nullable=False)
