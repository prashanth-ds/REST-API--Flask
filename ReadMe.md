#REST API

Overview
---
Here Northwind dataset is used to perform the CRUD operations with the help of REST API using Flask and SQLAlchemy.

Testing
---
Here the provided [postman](https://drive.google.com/file/d/1LaKLHxnsPMxK2VxtiBbU91qRqYn020Ek/view?usp=sharing) collection is used to test the set of requests implementing all the CRUD operations on the mentioned tables.

Make sure you've inserted the data into the database (MySql here) before executing the set of requests from the postman collection.


HTTP Requests
---
All the API requests are made by sending a HTTP request using the below mentioned methods.

- `GET` Get a resource or a list of resources
- `POST` Create a new resource
- `PUT` Update a existing resource or create a new resource
- `DELETE` Delete a resource

In this API, while performing the POST and PUT methods, the body of the request must have a JSON payload, all of which have been discussed in the following sections.


HTTP Responses
---
The responses are split up into two types mainly,

- GET
   
   The GET requests returns whole requested object(s), if the sent HTTP request is valid.
   
   ```
   "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001ACF7607B50>, 'city': 'London', 
  'customer_id': 'AROUT', 'contact_title': 'Sales Representative', 'company_name': 'Around the Horn', 
  'fax': '(171) 555-6750', 'country': 'UK', 'region': 'NULL', 'address': '120 Hanover Sq.', 'contact_name': 'Thomas Hardy', 
  'phone': '(171) 555-7788', 'postal_code': 'WA1 1DP'}\""
   ```
   
   Else, it provides a error message stating the reason why the request couldn't be processed
   
   `{"message": "The Customer Id AROU not found."}`
   

- Other Requests (POST, PUT, DELETE)

    Other type of requests are mainly pertained to return a JSON message responding with the success/error messages.
    
    `{"message": "The Customer Id DSPPP deleted."}`
    
    
HTTP Response Codes
---
   
Each response will always returns one of the following HTTP status code:

- `200` `OK` The request was successfully completed
- `201` `Created` A new resource was successfully created
- `400` `Bad Reuest` The request was invalid
- `404` `Not Found` The requested resource was not found
- `500` `Internal Server Error` The request was not completed due to an internal error on the server side


Types of Request
---

###Customers

-   ####Get Customer
    -   ```GET customer/:customer_id```
    
        The above will return JSON about the customer.
        
        #####Example
           
        **Request:**
        
        ```http://127.0.0.1:5000/customers/AROUT```
        
        **Response:**
        ```
        "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000013F00B0BB50>, 'city': 'London', 
        'customer_id': 'AROUT', 'contact_title': 'Sales Representative', 'company_name': 'Around the Horn', 
        'fax': '(171) 555-6750', 'country': 'UK', 'region': 'NULL', 'address': '120 Hanover Sq.', 'contact_name': 'Thomas Hardy',
         'phone': '(171) 555-7788', 'postal_code': 'WA1 1DP'}\""
        ```

-   ####Get Customers
    -   ```GET customers```
    
        The above will return JSON about all customers.
        
        #####Example
           
        **Request:**
        
        ```http://127.0.0.1:5000/customers```
        
        **Response:**
        ```
        {
            "Customers": [
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001EA24416940>, 'city': 'Berlin', 
                'customer_id': 'ALFKI', 'contact_title': 'Sales Representative', 'company_name': 'Alfreds Futterkiste', 
                'fax': '030-0076545', 'country': 'Germany', 'region': 'NULL', 'address': 'Obere Str. 57', 'contact_name': 'Maria Anders', 
                'phone': '030-0074321', 'postal_code': '12209'}\"",
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001EA24433B80>, 'city': 'M\Ã\©xico D.F.', 
                'customer_id': 'ANATR', 'contact_title': 'Owner', 'company_name': 'Ana Trujillo Emparedados y helados', 
                'fax': '(5) 555-3745', 'country': 'Mexico', 'region': 'NULL', 'address': 'Avda. de la Constituci\Ã\³n 2222', 'contact_name': 'Ana Trujillo', 
                'phone': '(5) 555-4729', 'postal_code': '05021'}\"",
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001EA24433BB0>, 'city': 'M\Ã\©xico D.F.', 
                'customer_id': 'ANTON', 'contact_title': 'Owner', 'company_name': 'Antonio Moreno Taquer\Ã\\\\xada', 
                'fax': 'NULL', 'country': 'Mexico', 'region': 'NULL', 'address': 'Mataderos  2312', 'contact_name': 'Antonio Moreno', 
                'phone': '(5) 555-3932', 'postal_code': '05023'}\"",
                ...
                ...
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001EA24443DF0>, 'city': 'Warszawa', 
                'customer_id': 'WOLZA', 'contact_title': 'Owner', 'company_name': 'Wolski  Zajazd', 'fax': '(26) 642-7012', 
                'country': 'Poland', 'region': 'NULL', 'address': 'ul. Filtrowa 68', 'contact_name': 'Zbyszek Piestrzeniewicz', 
                'phone': '(26) 642-7012', 'postal_code': '01-012'}\""
            ]   
        }
        ```

-   ####POST Customer
    -   ```POST customer/:customer_id```
    
        The above will return JSON about the customer that was created.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/customers/DSPPP```        
                                                                                                                                                                                                                                                                    
        **Body:**
        ```
        {"customer_id": "DSPPP", "company_name": "Datagrokr", "contact_name": "Naveen Gainedi", "contact_title": "M.D", 
        "address": "Bell Air Drive 5th Floor, Mekhri Circle", "city": "Bangalore", "region": "Asia", 
        "postal_code": "560032", "country": "India", "phone": "080-12345678", "fax": "080-12345678"}
        ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        **Response:**
        ```
        "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10E77BC70>}\""
        ```
        

-   ####PUT Customer
    -   ```PUT customer/:customer_id```
    
        The above will return JSON object of the customer modified.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/customers/DSPPP```        
                                                                                                                                                                                                                                                                    
        **Body:**
        ```
        {"customer_id": "DSPPP", "company_name": "Datagrokr", "contact_name": "Naveen Gainedi", "contact_title": "Managing Director", 
        "address": "Bell Air Drive 5th Floor, Mekhri Circle", "city": "Bangalore", "region": "Asia", "postal_code": "560032", 
        "country": "India", "phone": "080-12345678", "fax": "080-12345678"}
        ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        **Response:**
        ```
        "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x00000291CAF71EE0>}\""
        ```

-   ####DELETE Customer
    -   ```DELETE customer/:customer_id```
    
        The above will return JSON message about the deleted customer.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/customers/DSPPP```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

        **Response:**
        ```
        {"message": "The Customer Id DSPPP deleted."}
        ```
   

###Products

-   ####Get Product
    -   ```GET products/:product_id```
    
        The above will return JSON about the product.
        
        #####Example
           
        **Request:**
        
        ```http://127.0.0.1:5000/products/7```
        
        **Response:**
        ```
        "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EA0C7F0>, 'discontinued': True, 
        'units_on_order': 0, 'unit_price': 30.0, 'category_id': 7, 'product_name': \\\"Uncle Bob's Organic Dried Pears\\\", 
        'reorder_level': 10, 'units_in_stock': 15, 'quantity_per_unit': '12 - 1 lb pkgs.', 'supplier_id': 3, 'product_id': 7}\""
        ```

-   ####Get Product
    -   ```GET products```
    
        The above will return JSON about all products.
        
        #####Example
           
        **Request:**
        
        ```http://127.0.0.1:5000/products```
        
        **Response:**
        ```
        {
            "Products": [
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EA40430>, 'discontinued': True, 
                'units_on_order': 0, 'unit_price': 18.0, 'category_id': 1, 'product_name': 'Chai', 'reorder_level': 10, 
                'units_in_stock': 39, 'quantity_per_unit': '10 boxes x 20 bags', 'supplier_id': 1, 'product_id': 1}\"",
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EA373D0>, 'discontinued': True, 
                'units_on_order': 40, 'unit_price': 19.0, 'category_id': 1, 'product_name': 'Chang', 'reorder_level': 25, 
                'units_in_stock': 17, 'quantity_per_unit': '24 - 12 oz bottles', 'supplier_id': 1, 'product_id': 2}\"",
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EA37400>, 'discontinued': True, 
                'units_on_order': 70, 'unit_price': 10.0, 'category_id': 2, 'product_name': 'Aniseed Syrup', 'reorder_level': 25, 
                'units_in_stock': 13, 'quantity_per_unit': '12 - 550 ml bottles', 'supplier_id': 1, 'product_id': 3}\"",
                ...
                ...
                "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EA51D90>, 'discontinued': True, 
                'units_on_order': 0, 'unit_price': 18.0, 'category_id': 1, 'product_name': 'Mashed Potatoes', 'reorder_level': 10, 
                'units_in_stock': 39, 'quantity_per_unit': '10 boxes x 20 bags', 'supplier_id': 7, 'product_id': 78}\""
            ]   
        }
        ```

-   ####POST Product
    -   ```POST products/:products_id```
    
        The above will return JSON about the product that was created.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/products/78```        
                                                                                                                                                                                                                                                                    
        **Body:**
        ```
        {"product_id": "78", "product_name": "Chai", "supplier_id": "7", "category_id": "1", "quantity_per_unit": "10 boxes x 20 bags", 
        "unit_price": "18.00", "units_in_stock": "39", "units_on_order": "0", "reorder_level": "10", "discontinued": "0"}
        ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        **Response:**
        ```
        "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10E9F79A0>}\""
        ```
        

-   ####PUT Product
    -   ```PUT products/:products_id```
    
        The above will return JSON object of the product modified.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/products/78```        
                                                                                                                                                                                                                                                                    
        **Body:**
        ```
        {"product_id": "78", "product_name": "Mashed Potatoes", "supplier_id": "7", "category_id": "1", "quantity_per_unit": "10 boxes x 20 bags", 
        "unit_price": "18.00", "units_in_stock": "39", "units_on_order": "0", "reorder_level": "10", "discontinued": "0"}
        ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        **Response:**
        ```
        "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EA3D5E0>}\""
        ```

-   ####DELETE Product
    -   ```DELETE products/:products_id```
    
        The above will return JSON message about the deleted product.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/products/78```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

        **Response:**
        ```
        {"message": "The Product Id 78 deleted."}
        ```
        
        
###Orders

-   ####Get Order
    -   ```GET order/:order_id```
    
        The above will return JSON about the order.
        
        #####Example
           
        **Request:**
        
        ```http://127.0.0.1:5000/orders/10256```
        
        **Response:**
        ```
        "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EA0C610>, 'ship_postal_code': '08737-363', 
        'ship_city': 'Resende', 'ship_name': 'Wellington Importadora', 'customer_id': 'WELLI', 'freight': 13.97, 
        'shipped_date': datetime.datetime(1996, 7, 17, 0, 0), 'order_date': datetime.datetime(1996, 7, 15, 0, 0), 
        'ship_country': 'Brazil', 'ship_region': 'SP', 'ship_address': 'Rua do Mercado 12', 'order_id': 10256, 'ship_via': 2, 
        'required_date': datetime.datetime(1996, 8, 12, 0, 0), 'employee_id': 3}"
        ```

-   ####Get Orders
    -   ```GET orders```
    
        The above will return JSON about all orders.
        
        #####Example
           
        **Request:**
        
        ```http://127.0.0.1:5000/orders```
        
        **Response:**
        ```
        {
            "Orders": [
                "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EB28BE0>, 'ship_postal_code': '51100', 
                'ship_city': 'Reims', 'ship_name': 'Vins et alcools Chevalier', 'customer_id': 'VINET', 'freight': 32.38, 
                'shipped_date': datetime.datetime(1996, 7, 16, 0, 0), 'order_date': datetime.datetime(1996, 7, 4, 0, 0), 
                'ship_country': 'France', 'ship_region': 'NULL', 'ship_address': \"59 rue de l'Abbaye\", 'order_id': 10248, 
                'ship_via': 3, 'required_date': datetime.datetime(1996, 8, 1, 0, 0), 'employee_id': 5}",
                "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EB36AF0>, 'ship_postal_code': '44087', 
                'ship_city': 'MÃ¼nster', 'ship_name': 'Toms SpezialitÃ¤ten', 'customer_id': 'TOMSP', 'freight': 11.61, 
                'shipped_date': datetime.datetime(1996, 7, 10, 0, 0), 'order_date': datetime.datetime(1996, 7, 5, 0, 0), 
                'ship_country': 'Germany', 'ship_region': 'NULL', 'ship_address': 'Luisenstr. 48', 'order_id': 10249, 
                'ship_via': 1, 'required_date': datetime.datetime(1996, 8, 16, 0, 0), 'employee_id': 6}",
                "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EB36B20>, 'ship_postal_code': '05454-876', 
                'ship_city': 'Rio de Janeiro', 'ship_name': 'Hanari Carnes', 'customer_id': 'HANAR', 'freight': 65.83, 
                'shipped_date': datetime.datetime(1996, 7, 12, 0, 0), 'order_date': datetime.datetime(1996, 7, 8, 0, 0), 
                'ship_country': 'Brazil', 'ship_region': 'RJ', 'ship_address': 'Rua do PaÃ§o 67', 'order_id': 10250, 
                'ship_via': 2, 'required_date': datetime.datetime(1996, 8, 5, 0, 0), 'employee_id': 4}",
                ...
                ...
                "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EBC2DC0>, 'ship_postal_code': '51100', 
                'ship_city': 'City', 'ship_name': 'Vins et alcools Chevalier', 'customer_id': 'WELLI', 'freight': 32.38, 
                'shipped_date': datetime.datetime(1996, 7, 16, 0, 0), 'order_date': datetime.datetime(1996, 7, 4, 0, 0), 
                'ship_country': 'France', 'ship_region': 'NULL', 'ship_address': \"59 rue de l'Abbaye\", 'order_id': 11078, 
                'ship_via': 1, 'required_date': datetime.datetime(1996, 8, 1, 0, 0), 'employee_id': 1}"
            ]   
        }
        ```

-   ####POST Order
    -   ```POST orders/:order_id```
    
        The above will return JSON about the order that was created.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/orders/10256```        
                                                                                                                                                                                                                                                                    
        **Body:**
        ```
        {"order_id": "11078", "customer_id": "WELLI", "employee_id": "9", "order_date": "1996-07-04 00:00:00.000", 
        "required_date": "1996-08-01 00:00:00.000", "shipped_date": "1996-07-16 00:00:00.000", "ship_via": "2", 
        "freight": "32.38", "ship_name": "Vins et alcools Chevalier", "ship_address": "59 rue de l'Abbaye", 
        "ship_city": "Reims", "ship_region": "NULL", "ship_postal_code": "51100", "ship_country": "France"}
        ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        **Response:**
        ```
        "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001F10EB3EDF0>}"
        ```
        

-   ####PUT Order
    -   ```PUT orders/:order_id```
    
        The above will return JSON object of the order modified.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/orders/11078```        
                                                                                                                                                                                                                                                                    
        **Body:**
        ```
        {"order_id": "11078", "customer_id": "WELLI", "employee_id": "1", "order_date": "1996-07-04 00:00:00.000", 
        "required_date": "1996-08-01 00:00:00.000", "shipped_date": "1996-07-16 00:00:00.000", "ship_via": "1", 
        "freight": "32.38", "ship_name": "Vins et alcools Chevalier", "ship_address": "59 rue de l'Abbaye", 
        "ship_city": "City", "ship_region": "NULL", "ship_postal_code": "51100", "ship_country": "France"}
        ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        **Response:**
        ```
        "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001FB7817B640>}"
        ```

-   ####DELETE Order
    -   ```DELETE orders/:order_id```
    
        The above will return JSON message about the deleted order.
        
        #####Example
           
        **Request:**
        ```http://127.0.0.1:5000/orders/11078```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

        **Response:**
        ```
        {"message": "The Order Id 11078 deleted."}
        ```
        
        
###Order Details

-   ####Get Order Details
    -   ```GET order-details/:order_id```
    
        The above will return JSON about the order details about the given order id.
        
        #####Example
           
        **Request:**
        
        ```http://127.0.0.1:5000/order-details/11077```
        
        **Response:**
        ```
        [
            "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001FE8D50A5E0>, 'unit_price': 19.0, 
            'order_id': 11077, 'quantity': 24, 'product_id': 2, 'id': 2131, 'discount': 0.2}\"",
            "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001FE8D50AB50>, 'unit_price': 10.0, 
            'order_id': 11077, 'quantity': 4, 'product_id': 3, 'id': 2132, 'discount': 0.0}\"",
            "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001FE8D50AB80>, 'unit_price': 22.0, 
            'order_id': 11077, 'quantity': 1, 'product_id': 4, 'id': 2133, 'discount': 0.0}\"",
            ..
            ..
            "\"{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001FE8D5177F0>, 'unit_price': 13.0, 
            'order_id': 11077, 'quantity': 2, 'product_id': 77, 'id': 2155, 'discount': 0.0}\""
        ]
        ```