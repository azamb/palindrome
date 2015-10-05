from sqlalchemy import create_engine
from db import model
from constants import PALINDROME_DB_URI


if __name__ == '__main__':
    engine = create_engine(PALINDROME_DB_URI, echo=True)
    model.Base.metadata.create_all(engine)
    engine.dispose()
