from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "asdf"
#nb: secret key should be imported from a file excluded from the git repo
api = Api(app)

jst = JWT(app, authenticate, identity)   # /auth

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        #https://docs.python.org/2/library/functions.html
        #filter(function, iterable) returns iterator?
        #next(iterator[, default]), nb: , default @ end is returned if iterable is empty.
        return {"item": item}, 200 if item else 404
        # digits after the json is interpreted by browser as http response code
        #nb: if x evaluates to true if x is not None, evaluates to false if x == None

    def post(self, name):
        #now impose unique name on adding/creating new item.
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message':"An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        #NB: this requires the content-type to be set to application/json and body to be json in the post request, o/wise error.
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        #tells this method the items generated is the global var items
        items = list(filter(lambda x: x['name'] != name, items))
        #overwrite list items with list where name has been removed.
        return {'message': 'item deleted'}


api.add_resource(Item, "/item/<string:name>")


class ItemList(Resource):
    def get(self):
        return {"items": items}
api.add_resource(ItemList, "/items")



class Home(Resource):
    def get(self):
        return{"message": "Connected"}

api.add_resource(Home, "/")
#test

app.run(debug=True, port=5000, host='0.0.0.0')

