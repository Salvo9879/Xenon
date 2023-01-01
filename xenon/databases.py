
# Import external modules
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    household_name = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    settings = db.Column(db.JSON, nullable=True)

    @property
    def password(self):
        raise AttributeError('Property \'password\' is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hashed_password, password)

class Apis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_url = db.Column(db.String, nullable=False)
    api_key = db.Column(db.String, nullable=False)
    api_name = db.Column(db.String, nullable=False, unique=True)
    parameters = db.Column(db.JSON, nullable=True)
    api_last_call_dt = db.Column(db.DateTime, nullable=True)
    api_last_call_data = db.Column(db.JSON, nullable=True)