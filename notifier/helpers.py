'''Notifier helper functions

Flow:

    requestSubscription
        Given notification information, add a subscription record
        and a contactinfo record if info doesn't already exist

    requestURL (by user when change needed)
        (?Generate a new security nonce and)
        send the security nonce via the requested notification method
        If the contact info doesn't exist, create it and proceed

***Automated processes

    doNotifications
        Automated process to send notifications

    sendText
        Handle sending SMS message

    (sendEmail not needed, since it is built into Django)


'''

from notifier.models import *


def requestURL(phoneNumber="", emailAddress=""):
    '''Send the user a change URL with nonce to make changes or verify

    Look for the phone number / email in the contactinfo table and add if it isn't already there
    :param phoneNumber:
    :param emailAddress:
    :return:
    '''
    #TODO: implent requestURL
    # if both phoneNumber and emailAddress are blank, then throw an exception


def requestSubscription(longitude, latitude, phoneNumber="", emailAddress=""):
    '''Create a subscription record by longitude and latitude with given phone or email

    :param longitude:
    :param latitude:
    :param phoneNumber:
    :param emailAddress:
    :return:
    '''
    #TODO: implement requestSubscription()



def SendText(phone, smstext):
    '''
    Send a text message using twilio

    :param phone:
    :param smstext:
    :return:
    '''
    #TODO: implement SendText()
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
    #TODO: implement doNotifications()
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
