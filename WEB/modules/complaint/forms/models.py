from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,IntegerField,SelectField,DateField,EmailField
from wtforms.validators import InputRequired,Length,Regexp,Email

class ComplaintForm(FlaskForm):
    id = SelectField('Enter user id: ' ,validators=[InputRequired()])
    firstname = StringField('Enter first name: ',validators=[InputRequired(),Length(max=45)])
    middlename = StringField('Enter middle name: ',validators=[InputRequired(),Length(max=45)])
    lastname = StringField('Enter last name: ',validators=[InputRequired(),Length(max=45)])
    email = EmailField('Enter Email: ',validators=[InputRequired(),Length(max=30)])
    mobile = StringField('Enter mobile:', validators=[InputRequired(),
                                            Length(max=20),
                                            Regexp(regex=r"^(\+91)[-]{1}\d{3}[-]{1}\d{3}[-]{1}\d{4}$", message="Valid phone number format is +91-xxx-xxx-xxxx")])
    address = StringField('Enter Address: ',validators=[InputRequired(),Length(max=100)])
    zipcode = IntegerField("Enter ZipCode: ",validators=[InputRequired()])
    status = SelectField('Enter Status: ',choices=[('active','ACTIVE'),('inactive','INACTIVE'),('blocked','BLOCKED')],validators=[InputRequired()])
    date_registered = DateField("Enter date registered: ",format='%Y-%m-%d',validators=[InputRequired()])

    def validate_zipcode(self,zipcode):
        if not len(str(zipcode.data))==6:
            raise ValueError('ZIPCODE must be of 6 DIGITS')

class EmailComplaintForm(FlaskForm):
    to = StringField('Recipient(s):',validators=[InputRequired(),Length(max=50)])
    subject = StringField('Subject: ',validators=[InputRequired(),Length(max=50)])
    message = TextAreaField('Message: ',render_kw={"rows":30,"cols":81},validators=[InputRequired()])