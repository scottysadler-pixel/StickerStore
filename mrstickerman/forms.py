from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class CheckoutForm(FlaskForm):
    # customer details
    firstname = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    
    # delivery address
    address = StringField('Street Address', validators=[DataRequired()])
    suburb = StringField('Suburb', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    
    # submit button
    submit = SubmitField('Complete Order')
