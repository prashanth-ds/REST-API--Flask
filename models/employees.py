from db import db
import json
from datetime import datetime


class EmployeesModel(db.Model):

    __tablename__ = "employees"

    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    last_name = db.Column(db.String(20))
    first_name = db.Column(db.String(10))
    title = db.Column(db.String(30))
    title_of_courtesy = db.Column(db.String(25))
    birth_date = db.Column(db.DateTime())
    hire_date = db.Column(db.DateTime())
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    home_phone = db.Column(db.String(24))
    extension = db.Column(db.String(4))
    notes = db.Column(db.TEXT())
    reports_to = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), default=db.null())
    photo_path = db.Column(db.String(255))
    salary = db.Column(db.Float(precision=4))
    employees = db.relationship('EmployeesModel')

    def __init__(self, **args):

        def convert_datetime(date):
            # from_date = datetime.strptime(date, '%m/%d/%Y %I:%M:%S %p')
            # return datetime.strftime(from_date, "%m/%d/%Y %H:%M:%S")

            # date = 1992-05-01 00:00:00.000

            return datetime.strptime(date[:-4], "%Y-%m-%d %H:%M:%S")

        self.employee_id = args['employee_id']
        self.last_name = args['last_name']
        self.first_name = args['first_name']
        self.title = args['title']
        self.title_of_courtesy = args['title_of_courtesy']
        self.birth_date = convert_datetime(args['birth_date'])
        self.hire_date = convert_datetime(args['hire_date'])
        self.address = args['address']
        self.city = args['city']
        self.region = args['region']
        self.postal_code = args['postal_code']
        self.country = args['country']
        self.home_phone = args['home_phone']
        self.extension = args['extension']
        self.notes = args['notes']
        self.reports_to = args['reports_to']
        self.photo_path = args['photo_path']
        self.salary = args['salary']
        print(dict(**args))

    def json(self):
        # this is used for the get request.
        return json.dumps(str(self.__dict__))

    @classmethod
    def find_by_order_id(cls, employee_id):
        return cls.query.filter_by(employee_id=employee_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
