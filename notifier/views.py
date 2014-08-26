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


class PhoneSettings(RequestContextMixin, TemplateView):
    pass
