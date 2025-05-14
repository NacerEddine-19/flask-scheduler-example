from app.entities.models import get_groups
from app.login.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.fields import EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from .. import db


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    age = IntegerField('Age')
    group = QuerySelectField('Group', query_factory=get_groups, allow_blank=False)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember password')


class RegisterForm(FlaskForm):
    admin = BooleanField('Admin')
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),
                                     EqualTo('password', message='Passwords must match')])


class ConfirmationForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired(), Email()])


class EmailForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired(), Email()])


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
