# On Xampp Create a database ShopOnlineDB
# Crete table products with five columns
# product_id (primary key autoincrement), product_name, product_desc, product_cost, product_brand
# Create a function to save product information to the table products on Xampp
# Save at least eight records to the database
# Create another function where you can search an item using their product_name, product_cost
# Search a product with a certain range in terms of cost, e.g. search_by_cost(300,500)
# upload the file to your GitHub account

import pymysql

connection = pymysql.connect(host="localhost", user="root", password="", database="ShopOnlineDB")
print("Connection successful!")


def insert(product_id, product_name, product_desc, product_cost, product_brand):
    cursor = connection.cursor()
    sql = "insert into products (product_id, product_name, " \
          "product_desc, product_cost, product_brand) values(%s,%s,%s,%s,%s)"
    cursor.execute(sql, (product_id, product_name, product_desc, product_cost, product_brand))
    connection.commit()
    print("Data Saved Successfully!")


# insert("10", "Ulefone Note 10", "2022 model", "10,500", "Ulefone")

def search(product_name, product_cost):
    cursor = connection.cursor()
    sql = "select * from products where product_name=%s and product_cost=%s"
    cursor.execute(sql, (product_name, product_cost))
    connection.commit()
    data = cursor.fetchall()
    print("Data retrieval was successful!")
    print("We found {}".format(data))

# search("Spark 8C", "14,000")

def search_by_cost(minimum_cost, maximum_cost):
    cursor = connection.cursor()
    sql = "select * from products where product_id between %s and %s"
    cursor.execute(sql, (minimum_cost, maximum_cost))
    connection.commit()
    cost_range= cursor.fetchall()
    print(f"The products found {cost_range}")

search_by_cost("4", "8")

