from django.shortcuts import render
from twilio.rest import TwilioRestClient
from ..bpzaroundme.settings import TWILIO_SID, TWILIO_AUTH, TWILIO_NUM

# Create your views here.

def test(self):
    client = TwilioRestClient(TWILIO_SID, TWILIO_AUTH)

    smstext = ""
    sms = ""
    client.messages.create(
        body=smstext,
        to=sms,
        from_=TWILIO_NUM,
    )


