from db import db
import json



class CategoriesModel(db.Model):

    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    category_name = db.Column(db.String(15))
    description = db.Column(db.TEXT)

    def __init__(self, **args):
        self.category_id = args['category_id']
        self.category_name = args['category_name']
        self.description = args['description']

    def json(self):
        # this is used for the get request.
        return json.dumps(str(self.__dict__))

    @classmethod
    def find_by_order_id(cls, category_id):
        return cls.query.filter_by(category_id=category_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

