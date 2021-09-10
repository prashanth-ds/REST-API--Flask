from flask_restful import Resource, reqparse
from models.employees import EmployeesModel
from db import db


class Employees(Resource):
    # here parser is not a self, as parser is not a instance of a class rather it belongs to the class.
    parser = reqparse.RequestParser()

    parser.add_argument('employee_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('first_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('title_of_courtesy',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('birth_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('hire_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('city',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('region',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('postal_code',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('country',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('home_phone',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('extension',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('notes',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('reports_to',
                        type=int,
                        required=True,
                        nullable=True,
                        default=db.null(),
                        help="This field cannot be left blank")

    parser.add_argument('photo_path',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('salary',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")

    # from here we see the methods for different types of requests.
    def get(self, employee_id):
        order = EmployeesModel.find_by_order_id(employee_id)
        if order:
            return order.json()
        return {'message': f'The Employee Id {employee_id} not found.'}, 404

    def post(self, employee_id):
        if EmployeesModel.find_by_order_id(employee_id):
            return {'message': f'The Employee Id {employee_id} is already present.'}

        insert_data = Employees.parser.parse_args()
        if insert_data['reports_to'] == "NULL":
            insert_data['reports'] = None

        print("Fdssafs")

        order = EmployeesModel(**insert_data)
        print(order.__dict__)
        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting the Employee.'}, 500
        return order.json(), 201

    def delete(self, employee_id):
        order = EmployeesModel.find_by_order_id(employee_id)
        if order:
            order.delete_from_db()
            return {'message': f'The Employee Id {employee_id} deleted.'}, 200
        else:
            return {'message': f'The Employee Id {employee_id} not found.'}, 404

    def put(self, employee_id):
        update_data = Employees.parser.parse_args()

        order = EmployeesModel.find_by_order_id(employee_id)

        if order is None:
            order = EmployeesModel(**update_data)
        else:
            try:
                for key in list(order.__dict__.keys()):
                    print(getattr(order, key))
                    if key == '_sa_instance_state':
                        continue
                    setattr(order, key, getattr(update_data, key))
            except:
                return {'message': f'An error occured trying to update the Employee Id {employee_id}.'}, 500

        order.save_to_db()
        return order.json()


