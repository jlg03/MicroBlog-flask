from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joel'}
    posts = [
        {
            'author': {'username': 'john'},
            'body': 'A beautiful day in Portland!'
        },
        {
            'author': {'username': 'Sarah'},
            'body': 'The avengers movie was so cool'
            
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
