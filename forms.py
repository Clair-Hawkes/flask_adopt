"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField


class AddPetForm(FlaskForm):
    """ Form for addsing pets """

    pet_name = StringField("Pet Name: ")
    species = StringField("Species: ")
    photo_url = StringField("Profile Pic: ")
    age = SelectField("Age: ",
                      choices=[
                        ('baby', 'Baby'),
                        ('young', 'Young'),
                        ('adult', 'Adult'),
                        ('senior', 'Senior')])
    notes = StringField("Notes: ")

    # ("age in ('baby', 'young', 'adult', 'senior')"),


# Pet name
# Species
# Photo URL
# Age SelectField
# Notes


# class AddSnackForm(FlaskForm):
#     """Form for adding snacks."""

#     name = StringField("Snack Name")
#     price = FloatField("Price in USD")
