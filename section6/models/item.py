from db import db
import traceback

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        #NB: name and price initialzed by the code above. id value exists but not passed to self.id here. L84 @ 10:20
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        try:
            return cls.query.filter_by(name=name).first()
        except:
            traceback.print_exc()
        #name of table in generated SQL is given by __tablename__
        #SELECT * from items where name=name LIMIT 1  (returns first row only)
        #http://docs.sqlalchemy.org/en/latest/orm/query.html
        #nb: can do cls.query.filter_by(name=name).filter_by(id=1)
        #or can do cls.query.filter_by(name=name, id=1)

    def save_to_db(self):
        #nb removed try except + error output
        try:
            db.session.add(self)
            db.session.commit()
        except:
            #print('self'+self, file=sys.stderr)
            traceback.print_exc()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
