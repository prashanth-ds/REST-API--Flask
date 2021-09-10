from db import db
import json
from datetime import datetime


class OrdersModel(db.Model):

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    customer_id = db.Column(db.String(5), db.ForeignKey('customers.customer_id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    order_date = db.Column(db.DateTime(), nullable=True, default=db.null())
    required_date = db.Column(db.DateTime(), nullable=True, default=db.null())
    shipped_date = db.Column(db.DateTime(), nullable=True, default=db.null())
    ship_via = db.Column(db.Integer, db.ForeignKey('shippers.shipper_id'))
    freight = db.Column(db.Float(precision=4))
    ship_name = db.Column(db.String(40))
    ship_address = db.Column(db.String(60))
    ship_city = db.Column(db.String(15))
    ship_region = db.Column(db.String(15))
    ship_postal_code = db.Column(db.String(10))
    ship_country = db.Column(db.String(15))
    customers = db.relationship('CustomersModel')
    employees = db.relationship('EmployeesModel')
    shippers = db.relationship('ShippersModel')

    def __init__(self, **args):

        def convert_datetime(date):
            # from_date = datetime.strptime(date, '%m/%d/%Y %I:%M:%S %p')
            # return datetime.strftime(from_date, "%m/%d/%Y %H:%M:%S")

            # date = 1992-05-01 00:00:00.000
            if date == "NULL":
                return None

            return datetime.strptime(date[:-4], "%Y-%m-%d %H:%M:%S")

        self.order_id = args['order_id']
        self.customer_id = args['customer_id']
        self.employee_id = args['employee_id']
        self.order_date = convert_datetime(args['order_date'])
        self.required_date = convert_datetime(args['required_date'])
        self.shipped_date = convert_datetime(args['shipped_date'])
        self.ship_via = args['ship_via']
        self.freight = args['freight']
        self.ship_name = args['ship_name']
        self.ship_address = args['ship_address']
        self.ship_city = args['ship_city']
        self.ship_region = args['ship_region']
        self.ship_postal_code = args['ship_postal_code']
        self.ship_country = args['ship_country']

    def json(self):
        # this is used for the get request.
        return str(self.__dict__)

    @classmethod
    def find_by_order_id(cls, order_id):
        return cls.query.filter_by(order_id=order_id).first()

    def save_to_db(self):
        print(self.__dict__)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
