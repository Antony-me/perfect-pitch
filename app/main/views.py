from flask import  render_template, url_for, flash, redirect
from . import main
from .forms import  CommentForm, AddPitch, LoginForm, UpdateProfile, AddPitch
from app.models import User,Pitch, Comments
from flask_login import login_required
from ..import db


@main.route("/")
# @main.route("/home")
def home():

    pitches = Pitch.query.all()

    return render_template('home.html', pitches=pitches)


@main.route("/about")
def about():

    return render_template('about.html', title = 'About')


#.....
@main.route('/user/<uname>')
@login_required
def profile(uname):

    img_file =url_for('static', filename='current_user.')
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
        new_pitch = Pitch(title = form.title.data, content= form.content.data, category=form.category.data)
        db.session.add(new_pitch)
        db.session.commit()

        flash(f'Your Pitch was created succesfully !', 'success')

        return redirect(url_for('main.home'))

    return render_template('auth/addpitch.html',form=form)


#adding a comment
@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    """ 
    Function to post comments 
    """
    
    form = CommentForm()
    title = 'post comment'
    pitches = Pitch.query.filter_by(id=id).first()

    if pitches is None:
         abort(404)

    if form.validate_on_submit():
        comment = form.opinion.data
        new_comment = Comments(comment = comment, user_id = current_user.id, pitches_id = pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.view_pitch', id = pitches.id))

    return render_template('comments.html', form = form, title = title)


main.route('/categories/<int:id>')
def category(id):
    category = PitchCategory.query.get(id)
    if category is None:
        abort(404)

    pitches=Pitch.get_pitches(id)
    return render_template('category.html', pitches=pitches, category=category)


@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():
    """
    View new group route function that returns a page with a form to create a category
    """
    
    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = PitchCategory(name = name)
        new_category.save_category()

        return redirect(url_for('.home'))

    title = 'New category'
    return render_template('new_category.html', category_form = form, title = title)


