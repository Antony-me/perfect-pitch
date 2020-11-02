from flask import  render_template, url_for, flash, redirect
from . import main
from .forms import  CommentForm, AddPitch, LoginForm, UpdateProfile, AddPitch 
from app.models import User,Pitch, Comments, Votes
from flask_login import login_required, current_user
from ..import db


pitchys[{
    'title': 'Test'
    'content':'Test'
    'category':'Tech'
}]


@main.route("/")
# @main.route("/home")
def home():

    # pitchys = Pitch.query.all()


    return render_template('home.html', pitches=pitchys)


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
        author = current_user.id
        new_pitch = Pitch(user_id=author, title = form.title.data, content= form.content.data, category=form.category.data)
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
        comment = form.comment.data
        new_comment = Comments(opinion = comment, user_id = current_user.id, pitches_id = pitches.id)
        new_comment.save_comment()
        return redirect(url_for('main.view_pitch', id = pitches.id))

    return render_template('comments.html', form = form, title = title)


main.route('/categories/<int:id>')
def category(id):
    category = PitchCategory.query.get(id)
    if category is None:
        abort(404)

    pitches=Pitch.get_pitches(id)
    return render_template('category.html', pitches=pitches, category=category)



#view single pitch alongside its comments
@main.route('/view-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
    """
    Function the returns a single pitch for a comment to be added
    """
    # all_category = PitchCategory.get_categories()
    pitchess = Pitch.query.get(id)

    if pitchess is None:
        abort(404)
    
    comment = Comments.get_comments(id)
    print(comment)
    count_likes = Votes.query.filter_by(pitches_id=id, vote=1).all()
    count_dislikes = Votes.query.filter_by(pitches_id=id, vote=2).all()
    return render_template('view-pitch.html', pitches = pitchess, comment = comment, count_likes=len(count_likes), count_dislikes=len(count_dislikes))


#Routes upvoting/downvoting pitches
@main.route('/pitch/upvote/<int:id>&<int:vote_type>')
@login_required
def upvote(id,vote_type):
    """
    View function that adds one to the vote_number column in the votes table
    """
    # Query for user
    votes = Votes.query.filter_by(user_id=current_user.id).all()
    to_str=f'{vote_type}:{current_user.id}:{id}'

    if not votes:
        new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
        new_vote.save_vote()
        flash('YOU HAVE VOTED', 'success')

    for vote in votes:
        if f'{vote}' == to_str:

            break
        else:   
            new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
            new_vote.save_vote()
           
            break

    return redirect(url_for('.view_pitch', id=id))