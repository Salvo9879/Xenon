
# Import external modules
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Users(db.Model):
    __bind_key__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    household_name = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    settings = db.Column(db.JSON, nullable=True)

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

class GoveeDB(db.Model):
    """ Stores the govee devices in a database. """

    __bind_key__ = 'govee'

    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String, nullable=False)
    device_id = db.Column(db.String, nullable=False)
    device_model = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"<- [{self.id}] - {self.device_name} - ID: {self.device_id} - MODEL: {self.device_model} ->"