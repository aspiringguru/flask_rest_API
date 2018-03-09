from flask import Flask #dont need request any more
from flask_restful import Resource #keep Resource for route to load root
from flask_restful import Api#, reqparse
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

#https://flask-restful.readthedocs.io/en/0.3.5/reqparse.html



app = Flask(__name__)
#app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
#nb: secret key should be imported from a file excluded from the git repo
api = Api(app)
jst = JWT(app, authenticate, identity)   # /auth




class Home(Resource):
    def get(self):
        return{"message": "Connected"}

api.add_resource(Home, "/")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
#test

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
