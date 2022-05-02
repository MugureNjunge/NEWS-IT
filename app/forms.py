from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class SearchForm(FlaskForm):

    submit = SubmitField('Submit')