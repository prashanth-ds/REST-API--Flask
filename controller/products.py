from flask_restful import Resource, reqparse
from models.products import ProductsModel


class Products(Resource):
    # here parser is not a self, as parser is not a instance of a class rather it belongs to the class.
    parser = reqparse.RequestParser()

    parser.add_argument('product_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('product_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('supplier_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('category_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('quantity_per_unit',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('unit_price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('units_in_stock',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('units_on_order',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('reorder_level',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('discontinued',
                        type=bool,
                        required=True,
                        help="This field cannot be left blank")

    # from here we see the methods for different types of requests.
    def get(self, product_id):
        order = ProductsModel.find_by_order_id(product_id)
        if order:
            return order.json()
        return {'message': f'The Product Id {product_id} not found.'}, 404

    def post(self, product_id):
        if ProductsModel.find_by_order_id(product_id):
            return {'message': f'The Product Id {product_id} is already present.'}

        insert_data = Products.parser.parse_args()

        order = ProductsModel(**insert_data)

        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting the Product.'}, 500
        return order.json(), 201

    def delete(self, product_id):
        order = ProductsModel.find_by_order_id(product_id)
        if order:
            order.delete_from_db()
            return {'message': f'The Product Id {product_id} deleted.'}, 200
        else:
            return {'message': f'The Product Id {product_id} not found.'}, 404

    def put(self, product_id):
        update_data = Products.parser.parse_args()

        order = ProductsModel.find_by_order_id(product_id)

        if order is None:
            order = ProductsModel(**update_data)
        else:
            try:
                for key in list(order.__dict__.keys()):
                    print(getattr(order, key))
                    if key == '_sa_instance_state':
                        continue
                    setattr(order, key, getattr(update_data, key))
            except:
                return {'message': f'An error occured trying to update the Product Id {product_id}.'}, 500

        order.save_to_db()
        return order.json()


class ProductsList(Resource):
    def get(self):
        return {'Products': [product.json() for product in ProductsModel.query.all()]}

