"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.column(db.Integer,
        primary_key=True,
        autoincremement=True)
    name = db.column(db.String(25),
        nullable=False)
    species = db.column(db.String(25),
        nullable=False)
    photo_url = db.column(db.Text,
        nullable=False,
        default='')
    age = db.column(db.String(10),
        db.CheckConstraint("age in ['baby', 'young', 'adult', 'senior']"),
        nullable=False)
    notes = db.column(db.Text,
        nullable=False,
        default='')



