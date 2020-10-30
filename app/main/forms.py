from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, TextAreaField, SelectField, validators 
from flask_wtf import FlaskForm


class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')],validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')



class LoginForm(FlaskForm):
  
    email = StringField('Email', validators=[Required()])

    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me?')
    

    submit = SubmitField('Login Up')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class AddPitch(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    content = TextAreaField('Your Pitch.',validators = [Required()])
    submit = SubmitField('Submit')

