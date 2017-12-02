from wtforms import Form, StringField
from wtforms import PasswordField, validators
from wtforms.fields.html5 import EmailField


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email    = StringField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
