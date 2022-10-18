# Send an SMS
# Generate a random number
# Integrate to the database
# AfrikaStalking

# Username and API key
# Username: modcom2022

# import africastalking


def send_sms(phone, message):
    import africastalking
    africastalking.initialize(
        username="joe2022",
        api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"
    )

    sms = africastalking.SMS
    recipient = [phone]
    sender = "AFRICASTKNG"

    try:
        response = sms.send(message, recipient)
        print(response)
    except Exception as error:
        print(error)


# send_sms("+254728689854", "Receive the sample message")

def generate_random():
    import string
    import random
    s = 4

    ran = "".join(random.choices(string.digits, k=s))
    print("The randomly generated string is :", ran)
    return str(ran)


generate_random()

# MPesa and emails(SMTP), check passwords

# Exception handling research

# OOP --> method overloading, method overriding


