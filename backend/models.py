from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import DB_NAME, DB_USER, DB_PASSWORD



#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)

database_name = DB_NAME
database_path = 'postgresql://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, 'localhost:5432', database_name)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# TODO: connect to a local postgresql database
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


"""
User

"""


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)


"""
User Details

"""


class User_Details(db.Model):
    __tablename__ = 'user_details'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    number = db.Column(db.String)
    address = db.Column(db.String)
    about = db.Column(db.String)
    motto = db.Column(db.String)
    user = db.Relationship("User", backref="user_details", lazy=True)


"""
Social Media

"""


class Social_media(db.Model):
    __tablename__ = 'social_medias'

    id = db.Column(db.Integer, primary_key=True)
    facebook = db.Column(db.String)
    instagram = db.Column(db.String)
    twitter = db.Column(db.String)
    address = db.Column(db.String)
    linkedin = db.Column(db.String)
    youtube = db.Column(db.String)
    user = db.Relationship("User", backref="social_medias", lazy=True)

"""
Avatar

"""


class Social_media(db.Model):
    __tablename__ = 'user_images'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column()
    user = db.Relationship("User", backref="user_images", lazy=True)


"""
Relationship

"""

Details_user = db.Table('detail_show',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('user_details_id', db.Integer, db.ForeignKey('user_details.id'), primary_key=True)
    )

Venue_show = db.Table('social_media_user',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('social_media_id', db.Integer, db.ForeignKey('social_media.id'), primary_key=True)
    )
