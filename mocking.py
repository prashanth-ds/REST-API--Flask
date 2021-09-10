import unittest
from unittest.mock import patch
from app import app
from db import db


class CustomersMockTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    @patch('app.app.test_client')
    def test_get_customer(self, MockClass):
        response = MockClass()
        response.get().status_code = 200  # this is configured to return status code of 200 let anything be the get request in the below line of code (Mocking).

        statuscode = response.get("/customers/COMMI").status_code  #
        expected = 200
        self.assertEqual(expected, statuscode)

    @patch('app.app.test_client')
    def test_get_customers(self, MockClass):
        response = MockClass()
        response.get().status_code = 200  # this is configured to return status code of 200 let anything be the get request in the below line of code (Mocking).

        statuscode = response.get("/customers").status_code  # we mock the status_code that we defined previously
        expected = 200
        self.assertEqual(expected, statuscode)

    @patch('app.app.test_client')
    def test_post_customer(self, MockClass):
        payload = {"customer_id": "DSPPP", "company_name": "Datagrokr", "contact_name": "Naveen Gainedi",
                   "contact_title": "M.D", "address": "Bell Air Drive 5th Floor, Mekhri Circle", "city": "Bangalore",
                   "region": "Asia", "postal_code": "560032", "country": "India", "phone": "080-12345678",
                   "fax": "080-12345678"}

        response = MockClass()
        response.post().status_code = 201

        statuscode = response.post("/customers/DSPPP", data=payload).status_code
        expected = 201

        self.assertEqual(expected, statuscode)  # Status code as 201 because we create a new record in the database

    @patch('app.app.test_client')
    def test_put_customer(self, MockClass):
        payload = {"customer_id": "DSPPP", "company_name": "Datagrokr", "contact_name": "Naveen Gainedi",
                   "contact_title": "Managing Director", "address": "Bell Air Drive 5th Floor, Mekhri Circle",
                   "city": "Bangalore", "region": "Asia", "postal_code": "560032", "country": "India",
                   "phone": "080-12345678", "fax": "080-12345678"}

        response = MockClass()
        response.put().status_code = 200

        statuscode = response.put("/customers/DSPPP", data=payload).status_code
        expected = 200

        self.assertEqual(expected, statuscode)  # Status code as 201 because we create a new record in the database

    @patch('app.app.test_client')
    def test_delete_customer(self, MockClass):
        response = MockClass()
        response.delete().status_code = 200

        statuscode = response.delete("/customers/DSPPP").status_code
        expected = 200

        self.assertEqual(expected, statuscode)


class ProductsMockTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    @patch('app.app.test_client')
    def test_get_customer(self, MockClass):
        response = MockClass()
        response.get().status_code = 200  # this is configured to return status code of 200 let anything be the get request in the below line of code (Mocking).

        statuscode = response.get("/products/7").status_code  #
        expected = 200
        self.assertEqual(expected, statuscode)

    @patch('app.app.test_client')
    def test_get_customers(self, MockClass):
        response = MockClass()
        response.get().status_code = 200  # this is configured to return status code of 200 let anything be the get request in the below line of code (Mocking).

        statuscode = response.get("/products").status_code  # we mock the status_code that we defined previously
        expected = 200
        self.assertEqual(expected, statuscode)

    @patch('app.app.test_client')
    def test_post_customer(self, MockClass):
        payload = {"product_id": "78", "product_name": "Chai", "supplier_id": "7", "category_id": "1",
                   "quantity_per_unit": "10 boxes x 20 bags", "unit_price": "18.00", "units_in_stock": "39",
                   "units_on_order": "0", "reorder_level": "10", "discontinued": "0"}

        response = MockClass()
        response.post().status_code = 201

        statuscode = response.post("/products/78", data=payload).status_code
        expected = 201

        self.assertEqual(expected, statuscode)  # Status code as 201 because we create a new record in the database

    @patch('app.app.test_client')
    def test_put_customer(self, MockClass):
        payload = {"product_id": "78", "product_name": "Mashed Potatoes", "supplier_id": "7", "category_id": "1",
                   "quantity_per_unit": "10 boxes x 20 bags", "unit_price": "18.00", "units_in_stock": "39",
                   "units_on_order": "0", "reorder_level": "10", "discontinued": "0"}

        response = MockClass()
        response.put().status_code = 200

        statuscode = response.put("/products/78", data=payload).status_code
        expected = 200

        self.assertEqual(expected, statuscode)  # Status code as 201 because we create a new record in the database

    @patch('app.app.test_client')
    def test_delete_customer(self, MockClass):
        response = MockClass()
        response.delete().status_code = 200

        statuscode = response.delete("/products/78").status_code
        expected = 200

        self.assertEqual(expected, statuscode)


class OrdersMockTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    @patch('app.app.test_client')
    def test_get_customer(self, MockClass):
        response = MockClass()
        response.get().status_code = 200  # this is configured to return status code of 200 let anything be the get request in the below line of code (Mocking).

        statuscode = response.get("/orders/10256").status_code  #
        expected = 200
        self.assertEqual(expected, statuscode)

    @patch('app.app.test_client')
    def test_get_customers(self, MockClass):
        response = MockClass()
        response.get().status_code = 200  # this is configured to return status code of 200 let anything be the get request in the below line of code (Mocking).

        statuscode = response.get("/orders").status_code  # we mock the status_code that we defined previously
        expected = 200
        self.assertEqual(expected, statuscode)

    @patch('app.app.test_client')
    def test_post_customer(self, MockClass):
        payload = {"order_id": "11078", "customer_id": "WELLI", "employee_id": "9",
                   "order_date": "1996-07-04 00:00:00.000", "required_date": "1996-08-01 00:00:00.000",
                   "shipped_date": "1996-07-16 00:00:00.000", "ship_via": "2", "freight": "32.38",
                   "ship_name": "Vins et alcools Chevalier", "ship_address": "59 rue de l'Abbaye", "ship_city": "Reims",
                   "ship_region": "NULL", "ship_postal_code": "51100", "ship_country": "France"}

        response = MockClass()
        response.post().status_code = 201

        statuscode = response.post("/orders/11078", data=payload).status_code
        expected = 201

        self.assertEqual(expected, statuscode)  # Status code as 201 because we create a new record in the database

    @patch('app.app.test_client')
    def test_put_customer(self, MockClass):
        payload = {"order_id": "11078", "customer_id": "WELLI", "employee_id": "1",
                   "order_date": "1996-07-04 00:00:00.000", "required_date": "1996-08-01 00:00:00.000",
                   "shipped_date": "1996-07-16 00:00:00.000", "ship_via": "1", "freight": "32.38",
                   "ship_name": "Vins et alcools Chevalier", "ship_address": "59 rue de l'Abbaye",
                   "ship_city": "City", "ship_region": "NULL", "ship_postal_code": "51100", "ship_country": "France"}

        response = MockClass()
        response.put().status_code = 200

        statuscode = response.put("/orders/11078", data=payload).status_code
        expected = 200

        self.assertEqual(expected, statuscode)  # Status code as 201 because we create a new record in the database

    @patch('app.app.test_client')
    def test_delete_customer(self, MockClass):
        response = MockClass()
        response.delete().status_code = 200

        statuscode = response.delete("/orders/11078").status_code
        expected = 200

        self.assertEqual(expected, statuscode)


class OrderDetailsMockTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    @patch('app.app.test_client')
    def test_get_order_details(self, MockClass):
        response = MockClass()
        response.get().status_code = 200

        statuscode = response.get("/order-details/11077").status_code
        expected = 200

        self.assertEqual(expected, statuscode)


if __name__ == "__main__":
    db.init_app(app)
    unittest.main()

