from flask_restful import Resource, reqparse
from models.order_details import OrderDetailsModel


class OrderDetails(Resource):
    # here parser is not a self, as parser is not a instance of a class rather it belongs to the class.
    parser = reqparse.RequestParser()

    parser.add_argument('id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('order_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('product_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('unit_price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('discount',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")

    # from here we see the methods for different types of requests.
    def get(self, order_id):
        order = OrderDetailsModel.find_by_order_id(order_id)
        print(order)
        if order:
            return [each_order.json() for each_order in order]
        return {'message': f'The  Id {order_id} not found.'}, 404

    def post(self, id):
        if OrderDetailsModel.find_by_order_id(id):
            return {'message': f'The  Id {id} is already present.'}

        insert_data = OrderDetails.parser.parse_args()

        print(insert_data.__dict__)

        order = OrderDetailsModel(**insert_data)

        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting the Order.'}, 500
        return order.json(), 201

    def delete(self, order_id):
        order = OrderDetailsModel.find_by_order_id(order_id)
        if order:
            order.delete_from_db()
            return {'message': f'The Order Id {order_id} deleted.'}, 200
        else:
            return {'message': f'The Order Id {order_id} not found.'}, 404

    def put(self, order_id):
        update_data = OrderDetails.parser.parse_args()

        order = OrderDetailsModel.find_by_order_id(order_id)

        if order is None:
            order = OrderDetailsModel(**update_data)
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



