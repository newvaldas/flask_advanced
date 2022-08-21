from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

import app


def get_pk(obj):
    return str(obj)


class TevasForm(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    pavarde = StringField("Pavardė", [DataRequired()])
    vaikai = QuerySelectMultipleField(
        query_factory=app.Vaikas.query.all, get_label="vardas", get_pk=get_pk
    )
    submit = SubmitField("Įvesti")


class VaikasForm(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    pavarde = StringField("Pavardė", [DataRequired()])
    tevai = QuerySelectMultipleField(
        query_factory=app.Tevas.query.all, get_label="vardas", get_pk=get_pk
    )
    submit = SubmitField("Įvesti")