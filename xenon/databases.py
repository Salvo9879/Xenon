
# Import external modules
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Users(db.Model):
    """ The database which managers users on the service. """

    __bind_key__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    household_name = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    settings = db.Column(db.JSON, nullable=True)

    govee_access_token = ''
    
    smh_access_token = ''

    spotify_access_token = ''
    spotify_country_code = ''
    spotify_request_token = ''

    @property
    def password(self) -> None:
        raise AttributeError('Property \'password\' is not a readable attribute')
    
    @password.setter
    def password(self, password: str) -> None:
        self.hashed_password = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.hashed_password, password)

    def __repr__(self) -> str:
        return f"<- [{self.id}] - {self.forename} {self.surname} - EMAIL: {self.email} HOUSEHOLD NAME: {self.household_name} ->"
