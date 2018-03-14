from db import db
import sys

#methods here are not called directly by api, called internally by resource

class StoreModel(db.Model):
    #http://flask-sqlalchemy.pocoo.org/2.3/models/
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))#assigns max number of characters
    items = db.relationship('ItemModel', lazy='dynamic')
    #nb: lazy='dynamic' required to reduce overhead of generate object for each item in item table
    #refer http://docs.sqlalchemy.org/en/latest/orm/collections.html
    #when we use lazy='dynamic', self.items (below) is no longer list of items.
    #now it is a query builder.
    #http://docs.sqlalchemy.org/en/latest/orm/query.html ie. can use the .all() & other methods on this page.
    #nb: tradeoff between speed of creating store vs speed of calling the json method.

    def __init__(self, name, price):
        self.name = name

    def json(self):
        #returns json representation of store and items in the store.
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
        #need the .all() above when , lazy='dynamic' is used

    @classmethod
    def find_by_name(cls, name):
        #SQLAlchemy.Model.query
        print('models.store.StoreModel.find_by_name({}) called.'.format(name), file=sys.stderr)
        #return cls.query.filter_by(name=name)
        return cls.query.filter_by(name=name).first()
        #return cls.query.filter_by(name=name).one()
        #SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        print('models.store.StoreModel.save_to_db() called.', file=sys.stderr)
        db.session.add(self)
        db.session.commit()
        #db = SQLAlchemy, SQLAlchemy.session.add
        #http://docs.sqlalchemy.org/en/latest/orm/session_api.html
        #nb: this does insert and update.

    def delete_from_db(self):
        print('models.store.StoreModel.delete_from_db() called.', file=sys.stderr)
        db.session.delete(self)
        db.session.commit()
