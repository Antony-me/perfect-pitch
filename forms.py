from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from flask_wtf import FlaskForm

class RegistartionForm(FlaskForm):
    username = StringField('username', validators=[Required()])

    email = StringField('Email', validators=[Required()])

    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password', validators =[Required(), EqualTo('password')])

    submit = SubmitField('sign Up')


class LoginForm(FlaskForm):
  
    email = StringField('Email', validators=[Required()])

    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me?')
    

    submit = SubmitField('Login Up')