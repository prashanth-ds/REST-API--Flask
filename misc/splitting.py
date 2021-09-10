import csv


employees = '''
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    last_name = db.Column(db.String(20))
    first_name = db.Column(db.String(10))
    title = db.Column(db.String(30))
    title_of_courtesy = db.Column(db.String(25))
    birth_date = db.Column(db.DateTime)
    hire_date = db.Column(db.DateTime)
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    home_phone = db.Column(db.String(24))
    extension = db.Column(db.String(24))
    notes = db.Column(db.TEXT)
    reports_to = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    photo_path = db.Column(db.String(255))
    employees = db.relationship('EmployeesModel')
    '''

categories = '''
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    category_name = db.Column(db.String(15))
    description = db.Column(db.TEXT)
    '''

products = '''
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    product_name = db.Column(db.String(40))
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    quantity_per_unit = db.Column(db.String(40))
    unit_price = db.Column(db.Float(precision=4))
    units_in_stock = db.Column(db.SmallInteger())
    units_on_order = db.Column(db.SmallInteger())
    reorder_level = db.Column(db.SmallInteger())
    discontinued = db.Column(db.Boolean)
    suppliers = db.relationship('SuppliersModel')
    categories = db.relationship('CategoriesModel')
    '''

customers = '''
    customer_id = db.Column(db.String(5), primary_key=True, autoincrement=False)
    company_name = db.Column(db.String(40))
    contact_name = db.Column(db.String(30))
    contact_title = db.Column(db.String(30))
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    phone = db.Column(db.String(24))
    fax = db.Column(db.String(24))
    '''

shippers = '''
    shipper_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    company_name = db.Column(db.String(40))
    phone = db.Column(db.Integer)
    '''

suppliers = '''
    supplier_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    company_name = db.Column(db.String(40))
    contact_name = db.Column(db.String(30))
    contact_title = db.Column(db.String(30))
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    phone = db.Column(db.String(24))
    fax = db.Column(db.String(24))
    home_page = db.Column(db.TEXT)
    '''

orders = '''
order_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    customer_id = db.Column(db.String(5), db.ForeignKey('customers.customer_id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    order_date = db.Column(db.DateTime)
    required_date = db.Column(db.DateTime)
    shipped_date = db.Column(db.DateTime)
    ship_via = db.Column(db.Integer, db.ForeignKey('shippers.shipper_id'))
    freight = db.Column(db.Float(precision=4))
    ship_name = db.Column(db.String(40))
    ship_address = db.Column(db.String(60))
    ship_city = db.Column(db.String(15))
    ship_region = db.Column(db.String(15))
    ship_postal_code = db.Column(db.String(10))
    ship_country = db.Column(db.String(15))
    shippers = db.relationship('ShippersModel')
    customers = db.relationship('CustomersModel')
    employees = db.relationship('EmployeesModel')
    '''

variables = [orders, products, employees, customers, categories, shippers, suppliers]

for var in variables:

    add_comma = var.replace("\n", "$")
    split1 = add_comma.split('$')

    variable_name = []
    for row in split1:
        variable_name.append(row.split('=')[0].strip()) # this line splits each line of previous string using '=' and gets the variable name as it even strips the spaces


head_varibles = {'orders': ['order_id', 'customer_id', 'employee_id', 'order_date', 'required_date', 'shipped_date', 'ship_via', 'freight', 'ship_name', 'ship_address', 'ship_city', 'ship_region', 'ship_postal_code', 'ship_country', 'shippers', 'customers'],
                 'products': ['product_id', 'product_name', 'supplier_id', 'category_id', 'quantity_per_unit', 'unit_price', 'units_in_stock', 'units_on_order', 'reorder_level', 'discontinued'],
                 'employees': ['employee_id', 'last_name', 'first_name', 'title', 'title_of_courtesy', 'birth_date', 'hire_date', 'address', 'city', 'region', 'postal_code', 'country', 'home_phone', 'extension', 'notes', 'reports_to', 'photo_path'],
                 'customers': ['customer_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax'],
                 'category': ['category_id', 'category_name', 'description'],
                 'shippers': ['shipper_id', 'company_name', 'phone'],
                 'suppliers': ['supplier_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax', 'home_page']}

print(list(head_varibles.keys()))
