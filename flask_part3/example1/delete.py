from app import Message, db

bronius = Message.query.get(1)
db.session.delete(bronius)
db.session.commit()
print(Message.query.all())

