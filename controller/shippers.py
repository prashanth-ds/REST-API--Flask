from flask_restful import Resource, reqparse
from models.shippers import ShippersModel

class Shippers(Resource):
    # here parser is not a self, as parser is not a instance of a class rather it belongs to the class.
    parser = reqparse.RequestParser()

    parser.add_argument('shipper_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('company_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('phone',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    # from here we see the methods for different types of requests.
    def get(self, shipper_id):
        order = ShippersModel.find_by_order_id(shipper_id)
        if order:
            return order.json()
        return {'message': f'The Shipper Id {shipper_id} not found.'}, 404

    def post(self, shipper_id):
        if ShippersModel.find_by_order_id(shipper_id):
            return {'message': f'The Shipper Id {shipper_id} is already present.'}

        insert_data = Shippers.parser.parse_args()

        order = ShippersModel(**insert_data)

        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting the Shipper.'}, 500
        return order.json(), 201

    def delete(self, shipper_id):
        order = ShippersModel.find_by_order_id(shipper_id)
        if order:
            order.delete_from_db()
            return {'message': f'The Shipper Id {shipper_id} deleted.'}, 200
        else:
            return {'message': f'The Shipper Id {shipper_id} not found.'}, 404

    def put(self, shipper_id):
        update_data = Shippers.parser.parse_args()

        order = ShippersModel.find_by_order_id(shipper_id)

        if order is None:
            order = ShippersModel(**update_data)
        else:
            try:
                for key in list(order.__dict__.keys()):
                    print(getattr(order, key))
                    if key == '_sa_instance_state':
                        continue
                    setattr(order, key, getattr(update_data, key))
            except:
                return {'message': f'An error occured trying to update the Shipper Id {shipper_id}.'}, 500

        order.save_to_db()
        return order.json()


