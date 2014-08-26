from twilio.rest import TwilioRestClient
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from notifier.models import *


class RequestContextMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(RequestContextMixin, self).get_context_data(**kwargs)
        ctx['request'] = self.request
        return ctx


def SendText(self, phone, smstext):
    '''
    Send a text message using twilio

    :param phone:
    :param smstext:
    :return:
    '''
    client = TwilioRestClient(settings.TWILIO_SID, settings.TWILIO_AUTH)

    client.messages.create(
        body=smstext,
        to=phone,
        from_=settings.TWILIO_NUM
    )


def changeSettings(request, nonce=""):
    '''Use emailed or texted URL to modify settings
    Check incoming nonce against email or SMS to allow settings to be changed

    This same URL is used to verify an email or a phone number. If
    merge duplicate records in DB if phone number and email match up (?)
    :param request:
    :return:
    '''


def incomingSMS(request):
    '''
    Handle incoming SMS message from twilio
    :param request:
    :return:
    '''


