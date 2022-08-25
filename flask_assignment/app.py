import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import forms

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, "studentai_destytojai_paskaitos.db"
    )

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

association_table = db.Table('association', db.metadata,
    db.Column('tevas_id', db.Integer, db.ForeignKey('tevas.id')),
    db.Column('vaikas_id', db.Integer, db.ForeignKey('vaikas.id'))
)

class Lesson(db.model):
    __tablename__ = "paskaita"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column("Subject", db.String)
    professor_id = db.Column(db.Integer, db.ForeignKey("professor.id"))
    professor = db.relationship("Professor", backref="lessons")
    
    def __init__(self, subject, professor_id) -> None:
        self.subject = subject
        self.professor_id = professor_id

class Professor(db.Model):
    __tablename__ = "professor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String)
    surname = db.Column("Surname", db.String)
    
    
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    
    
