from enum import unique
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# pilnas kelias iki šio failo.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# nustatėme, kad mūsų duomenų bazė bus šalia šio failo esants data.sqlite failas

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# neseksime kiekvienos modifikacijos

db = SQLAlchemy(app)
Migrate(app, db) # <- stebi pasikeitimus tarp appso ir DB

# sukuriame duomenų bazės objektą
# sukurkime modelį užklausos formai, kuris sukurs duomenų bazėje lentelę


class Message(db.Model):
    # DB lentelei priskiria pavadinimą, jei nenurodysite, priskirs automatiškai pagal klasės pavadinimą.
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)  # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(40), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=True)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message, phone, age):
        self.name = name
        self.email = email
        self.message = message
        self.phone = phone
        self.age = age

    def __repr__(self):
        return f'{self.name} - {self.email} - {self.message} - {self.phone} - {self.age}'