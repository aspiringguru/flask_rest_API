from db import db
import sys

#methods here are not called directly by api, called internally by resource

class ItemModel(db.Model):
    #http://flask-sqlalchemy.pocoo.org/2.3/models/
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    #NB: id column added in L84 @ 7:20
    name = db.Column(db.String(80))#assigns max number of characters
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        #SQLAlchemy.Model.query
        print('models.item.ItemModel.find_by_name({}) called.'.format(name), file=sys.stderr)
        #return cls.query.filter_by(name=name)
        return cls.query.filter_by(name=name).first()
        #return cls.query.filter_by(name=name).one()
        #SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        #db = SQLAlchemy, SQLAlchemy.session.add
        #http://docs.sqlalchemy.org/en/latest/orm/session_api.html
        #nb: this does insert and update.

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
