import sqlite3
from db import db

class UserModel(object):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # NB: since find_by_username does not use self, make it a classmethod
    @classmethod
    def find_by_username(cls, username):
        #nb: either returns a User object or a None object
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))
        #NB: cursor.execute requires the second argument to be a tuple
        # hence comma after username.
        row = result.fetchone()
        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row)
            #*row notation is equivalent to row[0], row[1], row[2]
            #* collects all the positional arguments in a tuple
            #nb: columns in database correspond to User(_id, username, password)
        else:
            user = None
        connection.close()
        return user


    @classmethod
    def find_by_id(cls, _id):
        #nb: either returns a User object or a None object
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))
        #NB: cursor.execute requires the second argument to be a tuple
        # hence comma after username.
        row = result.fetchone()
        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row)
            #*row notation is equivalent to row[0], row[1], row[2]
            #* collects all the positional arguments in a tuple
            #nb: columns in database correspond to User(_id, username, password)
        else:
            user = None
        connection.close()
        return user
