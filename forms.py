from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField, BooleanField
from wtforms.validators import Required, Email, EqualTo

class RegistartionForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators =[DataRequired(), EqualTo('password')])

    submit = SubmitField('sign Up')


class LoginForm(FlaskForm):
  
    email = StringField('Email', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me?')
    

    submit = SubmitField('Login Up')