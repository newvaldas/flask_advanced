from app import Message, db
from random import randint

messages = Message.query.all()

for i in messages:
    random_phone = randint(999999, 10000000)
    i.phone = str(random_phone)
    db.session.add(i)

db.session.commit()

for x in messages:
    print (f'{x.id}, {x.name}, {x.email}, {x.phone}, {x.message}')
