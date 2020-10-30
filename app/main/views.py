from flask import  render_template, url_for, flash, redirect
from . import main
from .forms import  CommentForm, AddPitch, LoginForm
from app.models import User,Pitch, PitchCategory, Comments
from flask_login import login_required

pitches = [
    {
        'author': 'John Doe',
        'title': 'Pitch 1',
        'content': 'First pitch content',
        'date_posted': 'October 20, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Pitch 2',
        'content': 'Second pitch content',
        'date_posted': 'October 20, 2020'
    }
]

@main.route("/")
# @main.route("/home")
def home():

    return render_template('home.html', pitches=pitches)


@main.route("/about")
def about():

    return render_template('about.html', title = 'About')


@main.route('/pitch/new/<int:pitch_id>', methods = ['GET','POST'])
# @login_required
def new_pitch(id):

    form = AddPitch()
    
    return render_template('addpitch.html', title ='Addd Your Pitch', form=form)




# Login function
@main.route('/login',methods=['GET','POST'])
def login():
    """
    Function that checks if the form is validated
    """
    form = LoginForm()

    # if form.validate_on_submit():
    #     user = User.query.filter_by(email = login_form.email.data).first()
    #     if user is not None and user.verify_password(login_form.password.data):
    #         login_user(user,login_form.remember.data)
    #         return redirect(request.args.get('next')or url_for('main.index'))

    #     flash('Invalid Username or Password')

    return render_template('auth/login.html', form = form)

