import unittest
from app import app
from db import db


class CustomersUnitTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def test_get_customer(self):
        response = self.app.get("/customers/COMMI")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_customers(self):
        response = self.app.get("/customers")
        statuscode = response.status_code
        print(response.data)
        self.assertEqual(statuscode, 200)

    def test_post_customer(self):
        payload = {"customer_id": "DSPPP", "company_name": "Datagrokr", "contact_name": "Naveen Gainedi",
                   "contact_title": "M.D", "address": "Bell Air Drive 5th Floor, Mekhri Circle", "city": "Bangalore",
                   "region": "Asia", "postal_code": "560032", "country": "India", "phone": "080-12345678",
                   "fax": "080-12345678"}

        response = self.app.post("/customers/DSPPP", data=payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 201)  # Status code as 201 because we create a new record in the database

    def test_put_customer(self):
        payload = {"customer_id": "DSPPP", "company_name": "Datagrokr", "contact_name": "Naveen Gainedi",
                   "contact_title": "Managing Director", "address": "Bell Air Drive 5th Floor, Mekhri Circle",
                   "city": "Bangalore", "region": "Asia", "postal_code": "560032", "country": "India",
                   "phone": "080-12345678", "fax": "080-12345678"}

        response = self.app.put("/customers/DSPPP", data=payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_delete_customer(self):
        response = self.app.delete("/customers/DSPPP")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


class ProductsUnitTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def test_get_customer(self):
        response = self.app.get("/products/7")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_customers(self):
        response = self.app.get("/products")
        statuscode = response.status_code
        print(response.data)
        self.assertEqual(statuscode, 200)

    def test_post_customer(self):
        payload = {"product_id": "78", "product_name": "Chai", "supplier_id": "7", "category_id": "1",
                   "quantity_per_unit": "10 boxes x 20 bags", "unit_price": "18.00", "units_in_stock": "39",
                   "units_on_order": "0", "reorder_level": "10", "discontinued": "0"}

        response = self.app.post("/products/78", data=payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 201)  # Status code as 201 because we create a new record in the database

    def test_put_customer(self):
        payload = {"product_id": "78", "product_name": "Mashed Potatoes", "supplier_id": "7", "category_id": "1",
                   "quantity_per_unit": "10 boxes x 20 bags", "unit_price": "18.00", "units_in_stock": "39",
                   "units_on_order": "0", "reorder_level": "10", "discontinued": "0"}

        response = self.app.put("/products/78", data=payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_delete_customer(self):
        response = self.app.delete("/products/78")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


class OrdersUnitTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def test_get_customer(self):
        response = self.app.get("/orders/10256")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_customers(self):
        response = self.app.get("/orders")
        statuscode = response.status_code
        print(response.data)
        self.assertEqual(statuscode, 200)

    def test_post_customer(self):
        payload = {"order_id": "11078", "customer_id": "WELLI", "employee_id": "9",
                   "order_date": "1996-07-04 00:00:00.000", "required_date": "1996-08-01 00:00:00.000",
                   "shipped_date": "1996-07-16 00:00:00.000", "ship_via": "2", "freight": "32.38",
                   "ship_name": "Vins et alcools Chevalier", "ship_address": "59 rue de l'Abbaye", "ship_city": "Reims",
                   "ship_region": "NULL", "ship_postal_code": "51100", "ship_country": "France"}

        response = self.app.post("/orders/11078", data=payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 201)  # Status code as 201 because we create a new record in the database

    def test_put_customer(self):
        payload = {"order_id": "11078", "customer_id": "WELLI", "employee_id": "1",
                   "order_date": "1996-07-04 00:00:00.000", "required_date": "1996-08-01 00:00:00.000",
                   "shipped_date": "1996-07-16 00:00:00.000", "ship_via": "1", "freight": "32.38",
                   "ship_name": "Vins et alcools Chevalier", "ship_address": "59 rue de l'Abbaye",
                   "ship_city": "City", "ship_region": "NULL", "ship_postal_code": "51100", "ship_country": "France"}

        response = self.app.put("/orders/11078", data=payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_delete_customer(self):
        response = self.app.delete("/orders/11078")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


class OrderDetailsUnitTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def test_get_order_details(self):
        response = self.app.get("/order-details/11077")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == "__main__":
    db.init_app(app)
    unittest.main()

