import pymysql

dbconnection = pymysql.connect(host="localhost", user="root", password="", database="HospitalDB")


# print("connection successful")


def insert_patient():
    patient_name = str(input("Enter the patient's name: "))
    patient_age = str(input("Enter the patient's age: "))
    patient_gender = str(input("Enter the patient's gender: "))
    patient_diagnosis = str(input("What is the patient suffering from: "))
    patient_phone = str(input("Enter the patient's phone number: "))
    cursor = dbconnection.cursor()
    sql = "insert into patients (patient_name, patient_age, patient_gender, patient_diagnosis, patient_phone) values (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (patient_name, patient_age, patient_gender, patient_diagnosis, patient_phone))
    print("Record added successfully!")
    dbconnection.commit()
    send_sms(patient_phone, "Your details have been successfully added to the Modcom Hospital system")


# insert_patient()

def search_patient():
    patient_name = str(input("Enter the patient's name to search: "))
    patient_age = str(input("Enter the patient's age to search: "))
    cursor = dbconnection.cursor()
    sql = "select * from patients where patient_name=%s and patient_age=%s"
    cursor.execute(sql, (patient_name, patient_age))
    data = cursor.fetchone()
    if cursor.rowcount == 1:
        print("Patient found...")
        print("Patient Details...")
        print(f"Patient name is {data[1]}\n Patient admission date is {data[5]}\n "
              f"The patient is diagnosed with {data[4]}")
    else:
        print("Patient not found.")


# search_patient()

def delete_patient():
    patient_phone = str(input("Enter the phone number of the patient to delete +2547XXXXXXXX: "))
    cursor = dbconnection.cursor()
    sql = "delete from patients where patient_phone=%s"
    cursor.execute(sql, patient_phone)
    dbconnection.commit()

    print("Patient record deleted successfully!")


# delete_patient()

def update_patient():
    patient_name = str(input("Enter the patient's name to update: "))
    patient_age = str(input("Enter the patient's age to update: "))
    patient_gender = str(input("Enter the patient's gender to update: "))
    patient_diagnosis = str(input("What is the patient suffering from: "))
    patient_phone = str(input("Enter phone to update patient information: "))
    cursor = dbconnection.cursor()
    sql = "update patients set patient_name=%s, patient_age=%s, patient_gender=%s, patient_diagnosis=%s where patient_phone=%s"
    cursor.execute(sql, (patient_name, patient_age, patient_gender, patient_diagnosis, patient_phone))
    dbconnection.commit()


# update_patient()

import requests  # used for APIs
import base64  # data encryptions. Another one is called bycript
import datetime

from requests.auth import HTTPBasicAuth


def donate():
    phone = str(input("Enter your phone number to donate 2547XXXXXX: "))
    amount = int(input("Enter the amount you want to donate: "))
    consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
    consumer_secret = "amFbAoUByPV2rM5A"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    data = r.json()
    access_token = "Bearer" + ' ' + data['access_token']
    #  GETTING THE PASSWORD
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    business_short_code = "174379"
    data = business_short_code + passkey + timestamp
    encoded = base64.b64encode(data.encode())
    password = encoded.decode('utf-8')

    # BODY OR PAYLOAD
    payload = {
        "BusinessShortCode": "174379",
        "Password": "{}".format(password),
        "Timestamp": "{}".format(timestamp),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,  # use 1 when testing
        "PartyA": phone,  # change to your number
        "PartyB": "174379",
        "PhoneNumber": phone,
        "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
        "AccountReference": "Modcom",
        "TransactionDesc": "Modcom"
    }

    # POPULATING THE HTTP HEADER
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    print("Please check your phone to complete payment.")


# donate()

import africastalking


def send_sms(phone, message):
    africastalking.initialize(
        username="joe2022",
        api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"
        # justpaste.it/1nua8
    )
    sms = africastalking.SMS
    recipient = [phone]
    sender = "AFRICASTKNG"
    try:
        response = sms.send(message, recipient)
        print(response)
    except Exception as error:
        print("Execption is ", error)


send_sms("+254728689854", "Sample SMS")

# Numpy --> handling data that is in matrix format
# Pandas --> used for files: reading, viewing,
# matplotlib --> library for performing data visualization. Heatmaps, Charts, Graphs. Reporting/Data analysis
# Microsoft PowerBI, Tableau
# Sklearn library --> Getting insights, predictions, clustering data, regressions, classifications

# Data science steps
# 1. Fetching data
# 2. Data analysis (statistical analysis, checking outliers/anomalies, removing nulls, checking for redundancy)
# 3. Machine learning, Data mining
# 4. Model evaluation, testing phase --> accuracy score, r2score, precision, recall, confusion matrix
# 5. Model deployment (web applications, Android, cloud infrastructure e.g. AWS, Microsoft Azure)

