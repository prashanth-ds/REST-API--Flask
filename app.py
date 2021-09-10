from flask import Flask
from flask_restful import Api
from db import db
from controller.categories import Categories
from controller.shippers import Shippers
from controller.employees import Employees
from controller.suppliers import Suppliers
from controller.customers import Customers, CustomersList
from controller.orders import Orders, OrdersList
from controller.products import Products, ProductsList
from controller.order_details import OrderDetails


PORT = 5000
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sazclone123@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = "temporary"


@app.before_first_request
def create_table():
    db.create_all()


@app.route("/")
def home():
    return "Hello World"


api.add_resource(Customers, '/customers/<string:customer_id>')
api.add_resource(Suppliers, '/suppliers/<int:supplier_id>')
api.add_resource(Shippers, '/shippers/<int:shipper_id>')
api.add_resource(Products, '/products/<int:product_id>')
api.add_resource(Categories, '/categories/<int:category_id>')
api.add_resource(Employees, '/employees/<int:employee_id>')
api.add_resource(Orders, '/orders/<int:order_id>')
api.add_resource(CustomersList, '/customers')
api.add_resource(ProductsList, '/products')
api.add_resource(OrdersList, '/orders')

# api.add_resource(OrderDetails, '/order-details/<int:id>')
# uncomment above line, if inserting order-details and comment below line only when inserting.
api.add_resource(OrderDetails, '/order-details/<int:order_id>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=PORT, debug=True)

