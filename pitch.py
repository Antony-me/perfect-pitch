from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)
from forms import RegistartionForm , LoginForm

app.config['SECRET_KEY']= 'stuxnet993.'

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


@app.route("/")
def home():

    return render_template('home.html', pitches=pitches)


@app.route("/about")
def about():

    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistartionForm()
    if form.validate_on_submit():
        flask(f'Account Created for {form.username.data}!!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title ='Register', form=form)

@app.route("/login")
def login():

    form = LoginForm()

    return render_template('login.html', title ='Login', form=form)

    





if __name__ == "__main__":
    app.run(debug = True)