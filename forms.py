from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired

class Step1Form(FlaskForm):
    income = IntegerField('Monthly Income (₹)', validators=[DataRequired()])
    credit_score = SelectField('Credit Score', choices=[
        ('<600', '<600'), ('600-700', '600–700'), ('700+', '700+'), ('unknown', 'Unknown')])
    submit = SubmitField('Next')

class Step2Form(FlaskForm):
    fuel = IntegerField('Fuel (₹)', default=0)
    travel = IntegerField('Travel (₹)', default=0)
    groceries = IntegerField('Groceries (₹)', default=0)
    dining = IntegerField('Dining (₹)', default=0)
    submit = SubmitField('Next')

class Step3Form(FlaskForm):
    benefits = SelectMultipleField('Benefits',
        choices=[('cashback', 'Cashback'), ('travel', 'Travel Points'), ('lounge', 'Lounge Access')])
    submit = SubmitField('Next')

class Step4Form(FlaskForm):
    existing_cards = StringField('Any existing cards?')
    submit = SubmitField('Get Recommendations')