from flask_restful import Resource, reqparse
from models.orders import OrdersModel


class Orders(Resource):
    # here parser is not a self, as parser is not a instance of a class rather it belongs to the class.
    parser = reqparse.RequestParser()

    parser.add_argument('order_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('customer_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('employee_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('order_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('required_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('shipped_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('ship_via',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('freight',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('ship_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('ship_address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('ship_city',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('ship_region',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('ship_postal_code',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('ship_country',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    # from here we see the methods for different types of requests.
    def get(self, order_id):
        order = OrdersModel.find_by_order_id(order_id)
        if order:
            return order.json()
        return {'message': f'The Order Id {order_id} not found.'}, 404

    def post(self, order_id):
        if OrdersModel.find_by_order_id(order_id):
            return {'message': f'The Order Id {order_id} is already present.'}

        insert_data = Orders.parser.parse_args()

        order = OrdersModel(**insert_data)
        print(order.__dict__)
        print("prashanth")
        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting the order.'}, 500
        return order.json(), 201

    def delete(self, order_id):
        order = OrdersModel.find_by_order_id(order_id)
        if order:
            order.delete_from_db()
            return {'message': f'The Order Id {order_id} deleted.'}, 200
        else:
            return {'message': f'The Order Id {order_id} not found.'}, 404

    def put(self, order_id):
        update_data = Orders.parser.parse_args()

        order = OrdersModel.find_by_order_id(order_id)

        if order is None:
            order = OrdersModel(**update_data)
        else:
            try:
                for key in list(order.__dict__.keys()):
                    print(getattr(order, key))
                    if key == '_sa_instance_state':
                        continue
                    setattr(order, key, getattr(update_data, key))
            except:
                return {'message': f'An error occured trying to update the Order Id {order_id}.'}, 500

        order.save_to_db()
        return order.json()


class OrdersList(Resource):
    def get(self):
        return {'Orders': [order.json() for order in OrdersModel.query.all()]}

