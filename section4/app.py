from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
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

api.add_resource(Item, "/item/<string:name>")


class ItemList(Resource):
    def get(self):
        return {"items": items}
api.add_resource(ItemList, "/items")


class Store(Resource):
    def get(self, name):
        return {"store": name}

api.add_resource(Store, "/store/<string:name>")


class Home(Resource):
    def get(self):
        return{"message": "Connected"}

api.add_resource(Home, "/")
#test

app.run(debug=True, port=5000, host='0.0.0.0')

