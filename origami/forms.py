from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in checkout page
class CheckoutForm(FlaskForm):
    firstname = StringField("First name *", validators=[InputRequired()])
    surname = StringField("Last name *", validators=[InputRequired()])
    postcode = StringField("Postcode *", validators=[InputRequired()])
    address = StringField("Shipping address *", validators=[InputRequired()])
    email = StringField("Email *", validators=[InputRequired(), email()])
    phone = StringField("Phone number")
    request = StringField("Special Request (colors, gift wrapping etc..)")
    submit = SubmitField("Place Your Order!")

