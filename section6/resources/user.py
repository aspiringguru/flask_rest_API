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
        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        #type(user) = models/user.UserModel
        user.save_to_db()

        return{"message": "User created successfully."}, 201
        #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201
