from flask import Flask, render_template, url_for
app = Flask(__name__)
from forms import RegestartionForm, LoginForm

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
def hello():

    return render_template('home.html', pitches=pitches)


@app.route("/about")
def about():

    return render_template('about.html', title = 'About')

@app.route("/register")
def about():

    





if __name__ == "__main__":
    app.run(debug = True)