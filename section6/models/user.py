import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))#assigns max number of characters
    password = db.Column(db.String(80))#assigns max number of characters

    #def __init__(self, _id, username, password):
    def __init__(self, username, password):
        #id not required since the id is primary key and auto-incrementing.
        #these variables must match the variables defined above to be saved to database.
        #variables assigned to object in init not assigned to
        #SQLAlchemy.Model object wont be stored in database
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id)
        #nb: id's are unique, don't need first()
