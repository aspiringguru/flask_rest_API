import sqlite3
from flask_restful import Resource, reqparse

class User(object):
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


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    #https://flask-restful.readthedocs.io/en/0.3.6/api.html#module-reqparse

    parser.add_argument(    'username',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
    )
    parser.add_argument(    'password',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
    )


    def post (self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}
            
        #https://flask-restful.readthedocs.io/en/0.3.6/api.html#module-reqparse
        #parse_args(req=None, strict=False)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        #NULL since table users nominates field 'id'  as INTEGER PRIMARY KEY
        #ie: users.id is auto-incrementing
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return{"message": "User created successfully."}, 201
        #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201
