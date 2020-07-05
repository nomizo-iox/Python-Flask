from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Samuel Ademola',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Jordan Dockery',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    # Use 'Flash' message when user has registered sucessfully
    if register_form.validate():
        flash(f'Account created for {register_form.username.data}!', 'success')
        # The arguement inside 'URL_FOR', is the name of the function, and not html page
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'ademola1@gmail.com' and login_form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.  Please check username and passowrd', 'danger')
    return render_template('login.html', title='Login', form=login_form)
