from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def base_url():
    return "Hello world"

@app.route("/sms", methods=['GET', 'POST'])
def sms_general_reply():
    # Start our response
    resp = MessagingResponse()
    # Add a message
    resp.message("Thanks so much for your message. \
        This is all I can respond with at the moment.")
    return str(resp)