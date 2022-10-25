# Send an SMS
# Generate a random number
# Integrate to the database
# AfrikaStalking

# Username and API key
# Username: modcom2022

# import africastalking

#
# def send_sms(phone, message):
#     import africastalking
#     africastalking.initialize(
#         username="joe2022",
#         api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"
#     )
#
#     sms = africastalking.SMS
#     recipient = [phone]
#     sender = "AFRICASTKNG"
#
#     try:
#         response = sms.send(message, recipient)
#         print(response)
#     except Exception as error:
#         print(error)
#
#
# # send_sms("+254728689854", "Receive the sample message")
#
# def generate_random():
#     import string
#     import random
#     s = 4
#
#     ran = "".join(random.choices(string.digits, k=s))
#     print("The randomly generated string is :", ran)
#     return str(ran)
#

# generate_random()

# MPesa and emails(SMTP), check passwords

# Exception handling research

# OOP --> method overloading, method overriding


# Safaricom has a platforms for developers called Daraja API Portal

# API


def mpesa(phone, amount):
    import requests
    import base64
    import datetime
    from requests.auth import HTTPBasicAuth
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


mpesa(254728689854, 1)
