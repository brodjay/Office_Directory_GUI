from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FindIdForm(FlaskForm):
    id = StringField('Enter id: ', validators=[DataRequired()])
    submit = SubmitField('Search')

class FindNameForm(FlaskForm):
    firstname = StringField('Enter first name: ')
    lastname = StringField('Enter last name: ')
    submit = SubmitField('Search')

class AddUserForm(FlaskForm):
    id = StringField('ID: ', validators=[DataRequired()])
    firstname = StringField('First Name: ', validators=[DataRequired()])
    lastname = StringField('Last Name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    ipaddress = StringField('IP Address ', validators=[DataRequired()])
    submit = SubmitField('Add User')

class UpdateUserForm(FlaskForm):
    id = StringField('Enter id: ', validators=[DataRequired()])
    submit = SubmitField('Search')

class DeleteUserForm(FlaskForm):
    id = StringField('Enter id: ', validators=[DataRequired()])
    submit = SubmitField('Search')

class LoginUserForm(FlaskForm):
    username = StringField('Enter username: ', validators=[DataRequired()])
    submit = SubmitField('Login')