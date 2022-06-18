"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    """ Form for adding pets """

    pet_name = StringField("Pet Name: ",
      validators=[InputRequired()])

    species = StringField("Species: ",
      validators=[
        InputRequired(),
        AnyOf(
          ['dog','cat','porcupine'],
          message='Only dogs, cats, or porcupines allowed')])

    photo_url = StringField("Profile Pic: ",
      validators=[Optional(), URL(message="Must be valid url.")])

    age = SelectField("Age: ",
                      choices=[
                        ('baby', 'Baby'),
                        ('young', 'Young'),
                        ('adult', 'Adult'),
                        ('senior', 'Senior')])

    notes = StringField("Notes: ",
      validators=[Optional()])


class EditPetForm(FlaskForm):
    """ Form for editing pets """

    photo_url = StringField("Profile Pic: ",
        validators=[Optional(), URL(message="Must be valid url.")])

    notes = StringField("Notes: ",
      validators=[Optional()])

    #   TODO:Check defualt status, if required or optional, etc
    available = BooleanField('Avaiable: ')





















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
