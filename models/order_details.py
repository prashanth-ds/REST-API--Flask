from db import db
import json


class OrderDetailsModel(db.Model):

    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    unit_price = db.Column(db.Float(precision=4))
    quantity = db.Column(db.Integer)
    discount = db.Column(db.Float(precision=8))
    orders = db.relationship('OrdersModel')
    products = db.relationship('ProductsModel')

    def __init__(self, **args):
        self.id = args['id']
        self.order_id = args['order_id']
        self.product_id = args['product_id']
        self.unit_price = args['unit_price']
        self.quantity = args['quantity']
        self.discount = args['discount']

    def json(self):
        # this is used for the get request.
        return json.dumps(str(self.__dict__))

    @classmethod
    def find_by_order_id(cls, order_id):
        return cls.query.filter_by(order_id=order_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

