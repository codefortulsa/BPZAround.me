'''Views for notifications

    change user info
        Check that nonce is correct, otherwise "unauthorized"
        Add notification points / types
        Remove notification points / types
        Change contact address (email or phone)
        Add contact type (email / phone)

    incomingSMS
        Handle incoming SMS messages

'''
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.views.generic import TemplateView


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

    This same URL is used to verify an email or a phone number.

    Provide a place to enter an email address or phone number to link the two together


    :param request:
    :return:
    '''

    #TODO: need some way to link an existing phone and a separate existing email into one record, but not a blocking issue
    #TODO: implement user change view

def incomingSMS(request):
    '''
    Handle incoming SMS message from twilio
    :param request:
    :return:
    '''

    #TODO: handle incoming messages
