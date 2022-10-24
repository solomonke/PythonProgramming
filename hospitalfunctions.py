import pymysql

dbconnection = pymysql.connect(host="localhost", user="root", password="", database="HospitalDB")
print("connection successful")


def insert_patient():
    patient_name = str(input("Enter the patient's name: "))
    patient_age = str(input("Enter the patient's age: "))
    patient_gender = str(input("Enter the patient's gender: "))
    patient_diagnosis = str(input("What is the patient suffering from: "))
    cursor = dbconnection.cursor()
    sql = "insert into patients (patient_name, patient_age, patient_gender, patient_diagnosis) values (%s,%s,%s,%s)"
    cursor.execute(sql, (patient_name, patient_age, patient_gender, patient_diagnosis))
    dbconnection.commit()

insert_patient()



