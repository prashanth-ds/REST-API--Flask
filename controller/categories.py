from flask_restful import Resource, reqparse
from models.categories import CategoriesModel


class Categories(Resource):
    # here parser is not a self, as parser is not a instance of a class rather it belongs to the class.
    parser = reqparse.RequestParser()

    parser.add_argument('category_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('category_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    # from here we see the methods for different types of requests.
    def get(self, category_id):
        order = CategoriesModel.find_by_order_id(category_id)
        if order:
            return order.json()
        return {'message': f'The Category Id {category_id} not found.'}, 404

    def post(self, category_id):
        if CategoriesModel.find_by_order_id(category_id):
            return {'message': f'The Category Id {category_id} is already present.'}

        insert_data = Categories.parser.parse_args()

        order = CategoriesModel(**insert_data)

        try:
            order.save_to_db()
        except:
            return {'message': 'An error occured while inserting the Category.'}, 500
        return order.json(), 201

    def delete(self, category_id):
        order = CategoriesModel.find_by_order_id(category_id)
        if order:
            order.delete_from_db()
            return {'message': f'The Category Id {category_id} deleted.'}, 200
        else:
            return {'message': f'The Category Id {category_id} not found.'}, 404

    def put(self, category_id):
        update_data = Categories.parser.parse_args()

        order = CategoriesModel.find_by_order_id(int(category_id))

        if order is None:
            order = CategoriesModel(**update_data)
        else:
            try:
                print(update_data)
                print(order.__dict__)  # {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000013C4EC05040>, 'description': 'DS', 'category_id': 9, 'category_name': 'prashanth'}
                print(getattr(update_data, 'description'))

                for key in list(order.__dict__.keys()):
                    # if order.key == '_sa_instance_state':
                    #     continue
                    # order.key = update_data[key]
                    print(getattr(order, key))
                    if key == '_sa_instance_state':
                        continue
                    setattr(order, key, getattr(update_data, key))
            except:
                return {'message': f'An error occured trying to update the Category Id {category_id}.'}, 500

        order.save_to_db()
        return order.json()


