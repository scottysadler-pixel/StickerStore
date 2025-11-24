from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtorms.validators import DataRequired, Email

class CheckoutForm(FlaskForm):
    # Customer details
    firstname = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    
    # Submit button
    submit = SubmitField('Complete Order')
