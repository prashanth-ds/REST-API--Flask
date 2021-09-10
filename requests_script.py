import os
import requests
import json
import csv

csv_directory = 'Northwind_database_csv'
json_directory = 'Northwind_database_json'

# The below block of code (csv_to_json) is is to convert each csv file into json file of each csv file.

head_variables = {'orders.csv': ['order_id', 'customer_id', 'employee_id', 'order_date', 'required_date', 'shipped_date', 'ship_via', 'freight', 'ship_name', 'ship_address', 'ship_city', 'ship_region', 'ship_postal_code', 'ship_country', 'shippers', 'customers'],
                  'products.csv': ['product_id', 'product_name', 'supplier_id', 'category_id', 'quantity_per_unit', 'unit_price', 'units_in_stock', 'units_on_order', 'reorder_level', 'discontinued'],
                  'employees.csv': ['employee_id', 'last_name', 'first_name', 'title', 'title_of_courtesy', 'birth_date', 'hire_date', 'address', 'city', 'region', 'postal_code', 'country', 'home_phone', 'extension', 'notes', 'reports_to', 'photo_path', 'salary'],
                  'customers.csv': ['customer_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax'],
                  'categories.csv': ['category_id', 'category_name', 'description'],
                  'shippers.csv': ['shipper_id', 'company_name', 'phone'],
                  'order-details.csv': ['id', 'order_id', 'product_id', 'unit_price', 'quantity', 'discount'],
                  'suppliers.csv': ['supplier_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax', 'home_page']}


def manipulate_employees():
    modified = []
    store_ids = [0]

    with open("Northwind_database_csv/employees.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for test in reader:
            if not test:
                continue
            store_ids.append(int(test[0]))
        sorted(store_ids)

    with open("Northwind_database_csv/employees.csv", 'r') as file:
        reader = csv.reader(file)
        modified.append(next(reader))
        add_last = []

        print("prashanth")
        flag = 1

        for row in reader:
            if not row:
                continue

            if row[-3] == "NULL":
                row[-3] = row[0]
            print(row)
            # store_ids.append(row[0])

            if int(row[-3]) <= store_ids[flag]:  # this checks that whether the ReportsTo column is less than te store_ids, i.e. store_ids is ids of all rows, if at all the ReportTo column is less than or equal to the present row ID then we append, else we append at last. Because if raw data gets inserted into the database, there will be foreign key error.
            # if row[-3] in store_ids:
                modified.append(row)
            else:
                add_last.append(row)

            flag += 1

        for row in add_last:
            modified.append(row)

    with open('Northwind_database_csv/employees.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(modified)


def manipulate_order_details():
    final = []

    with open('Northwind_database_csv/order-details.csv', 'r') as file:
        reader = csv.reader(file)
        final.append(['id'] + next(reader))

        counter = 1
        for each_row in reader:
            if not each_row:
                continue
            final.append([counter] + each_row)
            counter += 1

    with open('Northwind_database_csv/order-details.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(final)


def csv_to_json():

    global csv_directory, head_variables

    # send_request_keys = list(head_variables.keys())
    files = os.listdir(csv_directory)

    exception = ['northwind-er-relationship.png']
    for each_file in files:
        if each_file not in exception:  # reomving the exceptions as of now
            with open(csv_directory+'/'+each_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # get the columns names

                json_data = {}
                for each_row in reader:
                    if not each_row:
                        continue

                    temp_dict = {}
                    id = ""
                    for index in range(len(each_row)):
                        if index == 0:
                            id = each_row[index]  # store the id from row, so that each complete record will be in

                        if each_file == "employees.csv" and each_row[index] == "NULL" and head_variables[each_file][index] == "reports_to":
                            print(8755132165484213)
                            print(each_row[index])
                            temp_dict[head_variables[each_file][index]] = each_row[0]

                            # this condition plays a very lethal role
                            each_row[index] = 0
                            print(head_variables[each_file][index], each_row[index])
                        else:
                            # below line of code will create a key value pair on the dict, where the key will retrieved from head_variables dict with file name sas key which retrieves the list of variables names and with index varibles we can loop every varibles.
                            temp_dict[head_variables[each_file][index]] = each_row[index]  # create a json object for each record using the head_variables generated above rather than first line of csv files for maintaining concurrency between request data and rest api attributes in each class

                    json_data[id] = temp_dict

            json_filename = each_file.split('.')[0] + ".json"
            with open(json_directory+'/'+json_filename, 'w') as file_object:
                json.dump(json_data, file_object)  # dump the whole dictionary as json object into the path


def requests_to_api():

    global json_directory

    # files = os.listdir(json_directory)  # just to avoid the the exception of error with this, next line works well
    files = ['categories.json', 'customers.json', 'suppliers.json', 'products.json', 'shippers.json', 'employees.json', 'orders.json', 'order-details.json']

    base_url = "http://127.0.0.1:5000/"

    for each_file in files:
        # if each_file in ["order-details.json"]:
        with open(json_directory + "/" + each_file, 'r') as file:
            json_data = json.load(file)
            print(json_data)

            sub_dir = each_file.split('.')[0]
            for key, value in json_data.items():
                # print(key, value)
                url = f"{base_url}{sub_dir}/{key}"
                # print(url)
                print(requests.post(url, data=value))
                # print(value)
            # print("done")


# manipulate_employees()
# manipulate_order_details()
# csv_to_json()
# requests_to_api()
