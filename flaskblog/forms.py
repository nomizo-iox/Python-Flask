# If Flask-wtf does not initially show up, make sure you do a pip3 install flask-wtf (brings in other modules)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class RegistrationForm(FlaskForm):
    # Validators ensure the validations of of user input
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=7, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    cnfm_password = PasswordField('Confirm Password', validators=[
                                  DataRequired(), EqualTo('password')])
    sumbit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    # Validators ensure the validations of of user input
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    sumbit = SubmitField('Login')
