import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
import sys, traceback



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        print('resources.user.UserRegister.post() called.', file=sys.stderr)
        try:
            data = UserRegister.parser.parse_args()
            print("data['username']= {}, data['password']={}".format(data['username'], data['password']), file=sys.stderr)

            if UserModel.find_by_username(data['username']):
                return {"message": "User with that username already exists."}, 400

            #user = UserModel(data['username'], data['password'])
            user = UserModel(**data)
            user.save_to_db()
            return {"message": "User created successfully."}, 201
        except:
            traceback.print_exc(file=sys.stderr)
            return {"message": "An error occurred in resources.user.UserRegister.post()."}, 500
