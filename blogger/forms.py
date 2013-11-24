
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo


class RegistrationForm(Form):
    __tablename__ = 'registrationForm'

    username = TextField('Username', [Required()])
    password = PasswordField('Password', [Required(), EqualTo('password_2', message='Passwords must match')])
    password_2 = PasswordField('Repeat Password')