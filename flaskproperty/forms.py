from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField,\
                    BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,\
                               ValidationError
from flaskproperty.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=2, max=10)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')])
    submit = SubmitField('Sign Up')

    # custom validators
    def validate_username(self, username):
        '''
        We make this function to prevent from error which is given by database.
        Check the username exist on database or not.
        '''
        seller = User.query.filter_by(username=username.data).first()
        if seller:
            raise ValidationError('username is taken')

    def validate_email(self, email):
        '''
        We make this function to prevent from error whish is given by database.
        Check the email exist on databse or not.
        '''
        seller = User.query.filter_by(email=email.data).first()
        if seller:
            raise ValidationError('gmail is taken')


class LoginForm(FlaskForm):
    email = StringField('Email address',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    location = StringField('Location',
                           validators=[DataRequired(), Length(min=2, max=30)])
    detail = TextAreaField('Detail',
                           validators=[DataRequired(),
                                       Length(min=50, max=500)])
    photo = FileField('Update Profile Picture',
                      validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')
