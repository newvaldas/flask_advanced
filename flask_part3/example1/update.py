from app import Message, db

user = Message.query.filter_by(name="Petras").first()# <- irasomas DB ID
print(user.message)
user.email = 'kazkoks@pastas.lt'
user.name = "Petrukas"
user.text = "Naujas postas"


db.session.add(user)
db.session.commit() # <- comitina pakeitina i DB
print(Message.query.all())

