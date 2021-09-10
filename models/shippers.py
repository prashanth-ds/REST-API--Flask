from db import db
import json


class ShippersModel(db.Model):

    __tablename__ = "shippers"

    shipper_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    company_name = db.Column(db.String(40))
    phone = db.Column(db.String(24))

    def __init__(self, **args):
        self.shipper_id = args['shipper_id']
        self.company_name = args['company_name']
        self.phone = args['phone']

    def json(self):
        # this is used for the get request.
        return json.dumps(str(self.__dict__))

    @classmethod
    def find_by_order_id(cls, shipper_id):
        return cls.query.filter_by(shipper_id=shipper_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
