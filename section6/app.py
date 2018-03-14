from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#turn off tracking because now using SQLAlchemy because it works better.
#http://flask-sqlalchemy.pocoo.org/2.3/config/
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db#import hereto avoid circular imports.
    db.init_app(app)
    app.run(debug=True, port=5000, host='0.0.0.0')  # important to mention debug=True
