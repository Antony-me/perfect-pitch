from flask import  render_template, url_for, flash, redirect
from . import main
from .forms import  CommentForm, AddPitch, LoginForm, UpdateProfile, AddPitch
from app.models import User,Pitch, Comments
from flask_login import login_required
from ..import db

# pitches = [
#     {
#         'author': 'John Doe',
#         'title': 'Pitch 1',
#         'content': 'First pitch content',
#         'date_posted': 'October 20, 2020'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Pitch 2',
#         'content': 'Second pitch content',
#         'date_posted': 'October 20, 2020'
#     }
# ]

@main.route("/")
# @main.route("/home")
def home():

    pitches = Pitch.query.all()

    return render_template('home.html', pitches=pitches)


@main.route("/about")
@login_required
def about():

    return render_template('about.html', title = 'About')


#.....
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/pitches/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = AddPitch()
    if form.validate_on_submit():
        author = 1

        new_pitch = Pitch(user_id=author, title = form.title.data, content= form.content.data, category=form.category.data)
        db.session.add(new_pitch)
        db.session.commit()

        flash(f'Your Pitch was created succesfully !', 'success')

        return redirect(url_for('main.home'))

    return render_template('auth/addpitch.html',form=form)




