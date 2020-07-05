from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Protects modifying cookies and crossight forgeries
app.config['SECRET_KEY'] = '649d7e67a5dfae7697963b041705565d'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://doadmin:dl41ga9bofbves9a@nomizodb-do-user-6621383-0.a.db.ondigitalocean.com/flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes