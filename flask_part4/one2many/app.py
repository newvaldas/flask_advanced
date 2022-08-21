import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

'''
Klasėje Book mus domina publisher_id kintamasis. Jis susieja klasę Book su klase Publisher per ForeignKey, 
kuriame parametruose nurodytas kitos lentelės pavadinimas ir prie kurio lauko rišame, t.y. prie id, 
kuris publishers lentelėje yra primary_key. 
'''
class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True) # primary_key unikalus ID kiekvienam naujam irasui
    author = db.Column(db.String(150))
    title = db.Column(db.String(300))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id')) #ForeignKey jungia i publisher lentele per id

    def __init__(self, author, title, publisher_id):
        self.author = author
        self.title = title
        self.publisher_id = publisher_id

    def __repr__(self):  # reprezentuoju tai kas pasirenkama pvz. title
        return self.title

'''
Klasėje Publisher, atgalinį ryšį su Books klase sukuria books kintamąjam priskirta eilutė. 
Parametruose nurodyta klasė, su kuria siejame ir backref - kol kas žiūrėkite, kaip į papildomą 
saitą tarp python klasių. 
'''
class Publisher(db.Model):

    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True) # 1 column
    name = db.Column(db.String(100), unique=True) # 2 column
    books = db.relationship('Book', backref='publisher')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    db.create_all()