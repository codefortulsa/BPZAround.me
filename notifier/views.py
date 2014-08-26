class RequestContextMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(RequestContextMixin, self).get_context_data(**kwargs)
        ctx['request'] = self.request
        return ctx


def changeSettings(request, nonce=""):
    '''Use emailed or texted URL to modify settings
    Check incoming nonce against email or SMS to allow settings to be changed

    This same URL is used to verify an email or a phone number.

    Provide a place to enter an email address or phone number to link the two together


    :param request:
    :return:
    '''

    #TODO: need some way to link an existing phone and a separate existing email into one record, but not a blocking issue


def incomingSMS(request):
    '''
    Handle incoming SMS message from twilio
    :param request:
    :return:
    '''


