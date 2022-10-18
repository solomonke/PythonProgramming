# Databases in Python
# MySQL DBMS

# Inserting and retrieving data from MySQL

# Open Xampp, create a database

# Modules for running MySQL is called pymysql

# Connect function requires four parameters: host, user, password for the database, database  name

from functions import send_sms, generate_random
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', database='PythonProjectDB')
print("Connection Successful")


# Create CRUD functions
# cursor() provides database functionalities in Python

def insert(user_id, user_name, user_email, user_password, phone_number):
    cursor = connection.cursor()

    if len(user_password) < 8:
        print("Password must have at least 8 digits")
    else:
        sql = 'insert into users (user_id, user_name, user_email, user_password, phone_number) values(%s,%s,%s,%s,%s)'
        cursor.execute(sql, (user_id, user_name, user_email, user_password, phone_number))
        connection.commit()

        print("Data Saved Successfully")


def retrieve(user_email, user_password):
    cursor = connection.cursor()
    sql = 'select * from users where user_email=%s and user_password=%s'
    cursor.execute(sql, (user_email, user_password))

    row = cursor.fetchone()
    phone = row[4]
    pin = generate_random()
    print(pin)
    send_sms(phone, "Successful, Your pin is {}".format(pin))
    if cursor.rowcount == 1:
        print("ACCESS GRANTED")
    elif cursor.rowcount == 0:
        print("Invalid credentials")
    else:
        print("Something wrong with your credentials")
    print(row)


retrieve("thisothermessage@gmail.com", "comMod20.9090")

# insert("20", "Karen", "thisothermessage@gmail.com", "comMod20.9090", "+254728689854")
# retrieve('reasonmail@gmail.com', 'comMod.90902777')


# Update, Delete Operations from CRUD

# def update(user_name, user_id):
#     cursor = connection.cursor()
#     sql = "update users set user_name=%s where user_id=%s"
#     cursor.execute(sql, (user_name, user_id))
#     connection.commit()
#     print("Data Updated Successfully!")


# update("John", "01")

# def delete(user_id):
#     cursor = connection.cursor()
#     sql = "delete from users where user_id=%s"
#     cursor.execute(sql, (user_id))
#     connection.commit()
#     print("Data Deleted Successfully!")

#
# delete("03")
