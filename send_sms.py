from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv(verbose=True)
import os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_MESSAGING_SERVICE_SID = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages \
    .create(
         body="Hello world\nFrom Sammie",
         messaging_service_sid=TWILIO_MESSAGING_SERVICE_SID,
         to=MY_PHONE_NUMBER
     )

print(message.sid)