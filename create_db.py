from application import db
from application.model import Messages

print('Creating Database')
db.create_all()
