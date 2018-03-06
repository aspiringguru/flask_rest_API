from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister


#https://flask-restful.readthedocs.io/en/0.3.5/reqparse.html



app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
#nb: secret key should be imported from a file excluded from the git repo
api = Api(app)

jst = JWT(app, authenticate, identity)   # /auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "This field cannot be left blank!"
    )

    @jwt_required() #when this route is in front of a method definition, the method requires authorisation to execute
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        #https://docs.python.org/2/library/functions.html
        #filter(function, iterable) returns iterator?
        #next(iterator[, default]), nb: , default @ end is returned if iterable is empty.
        return {"item": item}, 200 if item else 404
        # digits after the json is interpreted by browser as http response code
        #nb: if x evaluates to true if x is not None, evaluates to false if x == None

    #@jwt_required() #future implementation of login to post
    def post(self, name):
        #now impose unique name on adding/creating new item.
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message':"An item with name '{}' already exists".format(name)}, 400
        #by using an error first approach, the code below is not executed if error condition found.

        data = Item.parser.parse_args()
        #data = request.get_json() #ssd
        #NB: this requires the content-type to be set to application/json and body to be json in the post request, o/wise error.
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    @jwt_required() #future implementation of login to delete
    def delete(self, name):
        #todo: upgrade to return err msg if item does not exist to delete. curr version does not check
        global items
        #tells this method the items generated is the global var items
        items = list(filter(lambda x: x['name'] != name, items))
        #overwrite list items with list where name has been removed.
        return {'message': 'item deleted'}

    @jwt_required() #future implementation of login to put
    def put(self, name):
        #todo: replicate this in other methods.
        data = Item.parser.parse_args()
        #print (data['another']) #results in keyerror when tested in postman

        #data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
            #nb: data might contain a new name, bad, need to protect against this later
        return item

api.add_resource(Item, "/item/<string:name>")


class ItemList(Resource):
    def get(self):
        return {"items": items}
api.add_resource(ItemList, "/items")



class Home(Resource):
    def get(self):
        return{"message": "Connected"}

api.add_resource(Home, "/")
api.add_resource(UserRegister, "/register")
#test

app.run(debug=True, port=5000, host='0.0.0.0')
