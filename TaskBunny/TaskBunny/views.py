"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, abort
from TaskBunny import app

@app.route('/')
def home():
    if not session.get('logged_in'):
        print("going to login")
        return render_template('login.html')
    else:
        return render_template('layout.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

app = Flask(__name__)
 

 
@app.route('/login', methods=['POST'])
def do_admin_login():
    print("reached login")
    print(request.form['password'])
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()