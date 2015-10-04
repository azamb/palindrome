from application import db
from application.models import Message

print('Creating Database')
db.create_all()
