from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField,IntegerField
#from wtforms.validators import InputValidator

class LibraryForm(FlaskForm):
   # id= IntegerField('id')
    title = StringField('Tytuł')
    author = StringField('Autor')
    read = BooleanField('Czy przeczytane ?')