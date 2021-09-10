from flask_restful import Resource, reqparse
from models.suppliers import SuppliersModel


class Suppliers(Resource):
    # here parser is not a self, as parser is not a instance of a class rather it belongs to the class.
    parser = reqparse.RequestParser()

    parser.add_argument('supplier_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('company_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('contact_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('contact_title',
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

    parser.add_argument('phone',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('fax',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('home_page',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    # from here we see the methods for different types of requests.
    def get(self, supplier_id):
        order = SuppliersModel.find_by_order_id(supplier_id)
        if order:
            return order.json()
        return {'message': f'The Supplier Id {supplier_id} not found.'}, 404

    def post(self, supplier_id):
        if SuppliersModel.find_by_order_id(supplier_id):
            return {'message': f'The Supplier Id {supplier_id} is already present.'}

        insert_data = Suppliers.parser.parse_args()
        order = SuppliersModel(**insert_data)

        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting the Supplier.'}, 500
        return order.json(), 201

    def delete(self, supplier_id):
        order = SuppliersModel.find_by_order_id(supplier_id)
        if order:
            order.delete_from_db()
            return {'message': f'The Supplier Id {supplier_id} deleted.'}, 200
        else:
            return {'message': f'The Supplier Id {supplier_id} not found.'}, 404

    def put(self, supplier_id):
        update_data = Suppliers.parser.parse_args()

        order = SuppliersModel.find_by_order_id(supplier_id)

        if order is None:
            order = SuppliersModel(**update_data)
        else:
            try:
                for key in list(order.__dict__.keys()):
                    print(getattr(order, key))
                    if key == '_sa_instance_state':
                        continue
                    setattr(order, key, getattr(update_data, key))
            except:
                return {'message': f'An error occured trying to update the Supplier Id {supplier_id}.'}, 500

        order.save_to_db()
        return order.json()



