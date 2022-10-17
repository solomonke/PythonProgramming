# Databases in Python
# MySQL DBMS

# Inserting and retrieving data from MySQL

# Open Xampp, create a database

# Modules for running MySQL is called pymysql

# Connect function requires four parameters: host, user, password for the database, database  name

import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='PythonProjectDB')
print("Connection Successful")


# Create CRUD functions
# cursor() provides database functionalities in Python

def insert(user_id, user_name, user_email, user_password):
    cursor = connection.cursor()

    if len(user_password) < 8:
        print("Password must have at least 8 digits")
    else:
        sql = 'insert into users (user_id, user_name, user_email, user_password) values(%s,%s,%s,%s)'
        cursor.execute(sql, (user_id, user_name, user_email, user_password))
        connection.commit()

        print("Data Saved Successfully")


def retrieve(user_email, user_password):
    cursor = connection.cursor()
    sql = 'select * from users where user_email=%s and user_password=%s'
    cursor.execute(sql, (user_email, user_password))

    row = cursor.fetchone()
    if cursor.rowcount == 1:
        print("ACCESS GRANTED")
    elif cursor.rowcount == 0:
        print("Invalid credentials")
    else:
        print("Something wrong with your credentials")
    print(row)


# insert("11", "Hellen", "reasonmail@gmail.com", "comMod.90902777")
retrieve('reasonmail@gmail.com', 'comMod.90902777')
