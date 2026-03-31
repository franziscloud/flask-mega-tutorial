from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Franz'}
    posts = [
        { 
            'author': {'username': 'Czarina'},
            'body': 'Beautiful day in Rizal!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Ready or Not Part 2 Movie was so scary'
        },
        {
            'author': {'username': 'Franz'},
            'body': 'The 1Q84 is a long read'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)