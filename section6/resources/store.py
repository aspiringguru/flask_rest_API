from flask_restful import resource
from models.store import StoreModel

class Store(resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
            #nb: default return http code is 200, don't have to write explicity
        return {'message':'Store not found'}, 404

    def post(self, name):
        #not implementing this method because don't want to change store names
        #exists just to catch post requests(?)
        if StoreModel.find_by_name(name):
            return {'message': 'A store with name {} already exists.'.format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occurred while creating the store'}, 500
        return store.json(), 201

    def delete(self, name):
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
