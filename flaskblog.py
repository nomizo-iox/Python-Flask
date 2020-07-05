from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Protects modifying cookies and crossight forgeries
app.config['SECRET_KEY'] = '649d7e67a5dfae7697963b041705565d'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://doadmin:dl41ga9bofbves9a@nomizodb-do-user-6621383-0.a.db.ondigitalocean.com/flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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


if __name__ == "__main__":
    app.run(debug=True)
