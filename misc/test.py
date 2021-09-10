# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sazclone123@localhost/northwind'
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# admin = User('admin', 'admin@example.com')
#
# db.create_all() # In case user table doesn't exists already. Else remove it.
#
# db.session.add(admin)
#
# db.session.commit() # This is needed to write the changes to database
#
# User.query.all()
#
# print(User.query.filter_by(username='admin').first())
import csv
import json
from datetime import datetime


class Student:
    def __init__(self, *args):
        self.roll_no = args[0]
        self.name = args[1]
        self.batch = args[2]


class Car:
    def __init__(self, *args):
        self.brand = args[0]
        self.name = args[1]
        self.batch = args[2]


# main function
if __name__ == "__main__":
    # create two new student objects
    s1 = Student("85", "Swapnil", "IMT")
    s2 = Student("124", "Akash", "IMT")

    # create two new car objects
    c1 = Car("Honda", "city", "2005")
    c2 = Car("Honda", "Amaze", "2011")

    # convert to JSON format
    jsonstr1 = json.dumps(s1.__dict__)
    jsonstr2 = json.dumps(s2.__dict__)
    jsonstr3 = json.dumps(c1.__dict__)
    jsonstr4 = json.dumps(c2.__dict__)
    c2.__dict__['brand'] = "suzuki"
    json5 = c2.__dict__

    # print created JSON objects
    print(jsonstr1)
    print(jsonstr2)
    print(jsonstr3)
    print(json5['brand'])

    for k,v in c1.__dict__.items():
        print(k, v)

    date = datetime.strptime("1/9/1958  12:00:00 AM", '%m/%d/%Y %I:%M:%S %p')
    final = datetime.strftime(date, "%m/%d/%Y %H:%M:%S")

    print("1/9/1958  12:00:00 AM"[:-1])

    print(sorted([1,3,2,10,5,7]))

    with open("../Northwind_database_csv/orders.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        cust = []
        emp = []
        ship = []

        for row in reader:
            cust.append(row[1])
            emp.append(row[2])
            ship.append(row[6])

        print(sorted(set(cust)))
        print(set(emp))
        print(set(ship))