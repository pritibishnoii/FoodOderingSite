#from twilio.rest import Client
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sendsms():


    account_sid = "AC8621e769e445ec7cc0b062c148838986"
    auth_token = "3c8b6f8b5879d96bf3caf5bbc91d06a3"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body="hi this is test message",
    from_='+18167205166',
    to='9039515259',
    )

print('message send')