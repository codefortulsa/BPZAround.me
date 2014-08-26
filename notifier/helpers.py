from notifier.models import *


def requestURL(phoneNumber="", emailAddress=""):
    '''Send the user a change URL with nonce to make changes or verify

    Look for the phone number / email in the contactinfo table and add if it isn't already there
    :param phoneNumber:
    :param emailAddress:
    :return:
    '''

    # if both phoneNumber and emailAddress are blank, then throw an exception


def requestSubscription(longitude, latitude, phoneNumber="", emailAddress=""):
    '''Create a subscription record by longitude and latitude with given phone or email

    :param longitude:
    :param latitude:
    :param phoneNumber:
    :param emailAddress:
    :return:
    '''



def SendText(phone, smstext):
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


def doNotifications():
    '''Do all notifications
    Process all subscription records against geodata
    send email if provided
    send text if provided, acounting for rate limits

    :return:
    '''

    # check all notifications for nextNotification >= now

    #Set nextNotification to previous value plus default period (24 hours?)

    #send email if available

    #if phone # available:

    #(rate limiting logic for SMS)
    #if lastSMSSent is before today, reset NumSMSSentToday counter
    #check NumSMSSentToday. If below threshhold
    #increase NumSMSSentToday by 1
    #Is the NumSMSSentToday>limit if so, append limit warning to outbound SMS msg
    #send sms
