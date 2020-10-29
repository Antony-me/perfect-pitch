from flask import  render_template, url_for, flash, redirect
from . import main
from .forms import RegistartionForm , LoginForm, CommentForm, AddPitch
from app.models import User,Pitch, PitchCategory, Comments

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
def home():

    return render_template('home.html', pitches=pitches)


@main.route("/about")
def about():

    return render_template('about.html', title = 'About')

@main.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistartionForm()
    if form.validate_on_submit():
        flask(f'Account Created for {form.username.data}!!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title ='Register', form=form)

@main.route("/login")
def login():

    form = LoginForm()
    
    return render_template('login.html', title ='Login', form=form)


@main.route("/update")
def update():

    form = UpdateProfile()
    
    return render_template('update.html', title ='Login', form=form)

@main.route("/addpitch")
def addpitch():

    form = AddPitch()
    
    return render_template('addpitch.html', title ='Addd Your Pitch', form=form)



