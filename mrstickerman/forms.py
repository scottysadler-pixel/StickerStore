from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class CheckoutForm(FlaskForm):
    # Customer details
    firstname = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    
    # Delivery address
    address = StringField('Street Address', validators=[DataRequired()])
    suburb = StringField('Suburb', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    
    # Submit button
    submit = SubmitField('Complete Order')
