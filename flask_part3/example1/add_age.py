from app import Message, db
from random import randint

messages = Message.query.all()

for x in messages:
    random_age = randint(1, 90)
    x.age= str(random_age)
    db.session.add(x)

db.session.commit()

for x in messages:
    print (f'{x.id}, {x.name}, {x.email}, {x.phone}, {x.message}', {x.age})