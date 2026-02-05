from flask_wtf import FlaskForm
from wtforms import StringField,SelectMultipleField
from wtforms.validators import InputRequired,Length

class LoginForm(FlaskForm):
    username = StringField('Enter Username: ',validators=[InputRequired(),Length(min=5,max=45)])
    password = StringField('Enter Password: ',validators=[InputRequired(),Length(min=5,max=45)])
    user_type=SelectMultipleField('',
                                  choices={'User Types':[('1','Adminstrator'),('2','User')]},validators=[InputRequired()])

class LoginAuthForm(FlaskForm):
    username = StringField('Enter Username: ',validators=[InputRequired(),Length(min=5,max=45)])
    password = StringField('Enter Password: ',validators=[InputRequired(),Length(min=5,max=45)])
    