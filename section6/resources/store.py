from flask_restful import Resource
from models.store import StoreModel
import sys, traceback

class Store(Resource):
    def get(self, name):
        print('resources.store.Store.get({}) called.'.format(name), file=sys.stderr)
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
            #nb: default return http code is 200don't have to write explicity
        return {'message':'Store not found'}, 40

    def post(self, name):
        print('resources.store.Store.post({}) called.'.format(name), file=sys.stderr)
        #not implementing this method because don't want to change store names
        #exists just to catch post requests(?)
        if StoreModel.find_by_name(name):
            return {'message': 'A store with name {} already exists.'.format(name)}, 400
        else:
            print('resources.store.Store.post({}), store with name {} does not exist.'.format(name, name), file=sys.stderr)
        store = StoreModel(name)
        print('resources.store.Store.post({}), store with name {} created.'.format(name, name), file=sys.stderr)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occurred while creating the store'}, 500
        return store.json(), 201

    def delete(self, name):
        print('resources.store.Store.delete({}) called.'.format(name), file=sys.stderr)
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'store deleted'}
        else:
            return {'message': 'store does not exist.'}, 400

class StoreList(Resource):
    def get(self):
        return {'stores': [item.json() for item in StoreModel.query.all()]}
        #lambda version of above
        #return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}

    pass
