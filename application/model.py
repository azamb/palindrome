from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, Text, Boolean, func

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

    id = Column(Integer, primary_key=True)
    message = Column(Text, unique=False, nullable=False)
    username = Column(String(50), unique=False, nullable=False)
    created_on = Column(DateTime, default=func.now())
    is_palindrome = Column(Boolean, nullable=False)
