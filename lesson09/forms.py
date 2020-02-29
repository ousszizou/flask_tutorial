from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email

class MyForm(FlaskForm):
    email = StringField(label='Email address', validators=[ DataRequired(), Email() ])
    password = PasswordField(label='Password', validators=[ DataRequired() ])
