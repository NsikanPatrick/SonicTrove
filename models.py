from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

db = SQLAlchemy()

def db_setup(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    return db

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    # DONE: missing fields for the Venue table implemented

    genres = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    past_shows = db.Column(db.Integer, default=0)
    upcoming_shows = db.Column(db.Integer, default=0)
    shows = db.relationship('Show', backref='venue', lazy=True,
                            cascade="all, delete-orphan")

    def __repr__(self):
        return f"<id={self.id} name={self.name} city={self.city} address={self.address} phone={self.phone}> \n"


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    # DONE: missing fields for the Artist table implemented
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    past_shows = db.Column(db.Integer, default=0)
    upcoming_shows = db.Column(db.Integer, default=0)
    shows = db.relationship('Show', backref='artist', lazy=True,
                            cascade="all, delete-orphan")

    def __repr__(self):
        return f"<id={self.id} name={self.name} city={self.city} address={self.address} phone={self.phone}> \n"

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
# DONE: All model relationships completed


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.id'), nullable=False)
    start_time = db.Column(
        db.DateTime, nullable=False)