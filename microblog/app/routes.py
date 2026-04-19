from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)