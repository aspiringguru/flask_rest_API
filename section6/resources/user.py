import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

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

        if UserModel.find_by_username(data['username']):
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
