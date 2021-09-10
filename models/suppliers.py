from db import db
import json


class SuppliersModel(db.Model):

    __tablename__ = "suppliers"

    supplier_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    company_name = db.Column(db.String(40))
    contact_name = db.Column(db.String(30))
    contact_title = db.Column(db.String(30))
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    phone = db.Column(db.String(24))
    fax = db.Column(db.String(24))
    home_page = db.Column(db.TEXT)

    def __init__(self, **args):
        self.supplier_id = args['supplier_id']
        self.company_name = args['company_name']
        self.contact_name = args['contact_name']
        self.contact_title = args['contact_title']
        self.address = args['address']
        self.city = args['city']
        self.region = args['region']
        self.postal_code = args['postal_code']
        self.country = args['country']
        self.phone = args['phone']
        self.fax = args['fax']
        self.home_page = args['home_page']

    def json(self):
        # this is used for the get request.
        return json.dumps(str(self.__dict__))

    @classmethod
    def find_by_order_id(cls, supplier_id):
        return cls.query.filter_by(supplier_id=supplier_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
