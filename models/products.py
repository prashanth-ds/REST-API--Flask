from db import db
import json


class ProductsModel(db.Model):

    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    product_name = db.Column(db.String(40))
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    quantity_per_unit = db.Column(db.String(40))
    unit_price = db.Column(db.Float(precision=4))
    units_in_stock = db.Column(db.SmallInteger())
    units_on_order = db.Column(db.SmallInteger())
    reorder_level = db.Column(db.SmallInteger())
    discontinued = db.Column(db.Boolean)
    suppliers = db.relationship('SuppliersModel')
    categories = db.relationship('CategoriesModel')

    def __init__(self, **args):
        self.product_id = args['product_id']
        self.product_name = args['product_name']
        self.supplier_id = args['supplier_id']
        self.category_id = args['category_id']
        self.quantity_per_unit = args['quantity_per_unit']
        self.unit_price = args['unit_price']
        self.units_in_stock = args['units_in_stock']
        self.units_on_order = args['units_on_order']
        self.reorder_level = args['reorder_level']
        self.discontinued = args['discontinued']

    def json(self):
        # this is used for the get request.
        return json.dumps(str(self.__dict__))

    @classmethod
    def find_by_order_id(cls, product_id):
        return cls.query.filter_by(product_id=product_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
