"""Notifier helper functions

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


"""

from django.contrib.gis.measure import D
from django.core.mail import send_mail
from twilio.rest import TwilioRestClient
from bpz.models import BOACase, TMAPCCase
from notifier.models import *


def getcontact(phonenumber="", emailaddress=""):
    if (phonenumber is not None) and (emailaddress is not None):
        contact = ContactInfo.objects.get_or_create(phoneNumber=phonenumber, email=emailaddress)

    if (phonenumber is None) and (emailaddress is not None):
        contact = ContactInfo.objects.get_or_create(email=emailaddress)

    if (phonenumber is not None) and (emailaddress is None):
        contact = ContactInfo.objects.get_or_create(phoneNumber=phonenumber)

    if contact is None:
        return None
    else:
        return contact


def requesturl(phonenumber="", emailaddress=""):
    """Send the user a change URL with nonce to make changes or verify

    Look for the phone number / email in the contactinfo table and add if it isn't already there
    :param phonenumber:
    :param emailaddress:
    :return:
    """
    contact = getcontact(phonenumber, emailaddress)

    if contact is None:
        return

    contact.nonce = newnonce()
    contact.save()

    rtext = "Change your settings: http://zoningcases.com/update/%s" % contact.nonce
    if emailaddress is not None:
        send_mail("Change your settings on zoningcases.com",
                  rtext,
                  "noreply@zoningcases.com", [emailaddress],
                  fail_silently=False)
    if phonenumber is not None:
        sendtext(phonenumber, rtext)


def requestsubscription(longitude, latitude, stype, phonenumber="", emailaddress=""):
    """Create a subscription record by longitude and latitude with given phone or email

    :param longitude:
    :param latitude:
    :param stype:
    :param phonenumber:
    :param emailaddress:
    :return:
    """
    # TODO: implement requestSubscription()
    contact = getcontact(phonenumber, emailaddress)

    if contact is None:
        return

    thislocation = models.PointField()
    thislocation.srid = 4326
    thislocation.x = longitude
    thislocation.y = latitude
    thislocation.geography = True

    subscription = Subscription(contactInfo=contact,
                                subscriptionType=stype,
                                geom=thislocation)
    subscription.save()


def sendtext(phone, smstext):
    """
    Send a text message using twilio

    :param phone:
    :param smstext:
    :return:
    """
    # TODO: implement SendText()
    client = TwilioRestClient(settings.TWILIO_SID, settings.TWILIO_AUTH)

    client.messages.create(
        body=smstext,
        to=phone,
        from_=settings.TWILIO_NUM
    )


def donotifications():
    """Do all notifications
    Process all subscription records against geodata
    send email if provided
    send text if provided, acounting for rate limits

    :return:
    """
    # TODO: implement doNotifications()

    smsmsg = ""
    emailmsg = ""

    subscriptionrecords = Subscription.objects.filter(nextNotification__gtq=datetime.now())

    for subscriptionrecord in subscriptionrecords:
        # if subscriptionRecord.subscriptionType == 'N':
        # boaList = BOACase.objects.filter()
        #we don't have date/time oriented info for neighborhood associations

        #find everything for the upcoming x days
        if subscriptionrecord.subscriptionType == 'A':
            adjustmentrecords = BOACase.objects.filter(
                geom__distance_lte=(subscriptionrecord.geom,
                                    D(mi=subscriptionrecord.distance)))

            #TODO add BOA records to email using jinja2 template & text

        #find everything for the upcoming x days
        elif subscriptionrecord.subscriptionType == 'T':
            tmaprecords = TMAPCCase.objects.filter(
                geom__distance_lte=(subscriptionrecord.geom,
                                    D(mi=subscriptionrecord.distance)))

            #TODO add TMAP records to email using jinja2 template & text

        #Set nextNotification to previous value plus default period
        subscriptionrecord.nextNotification = datetime.now() + datetime.timedelta(days=1)
        subscriptionrecord.save()

        #send email if available

        #if phone # available:

        #(rate limiting logic for SMS)
        #if lastSMSSent is before today, reset NumSMSSentToday counter
        #check NumSMSSentToday. If below threshhold
        #increase NumSMSSentToday by 1
        #Is the NumSMSSentToday>limit if so, append limit warning to outbound SMS msg
        #send sms
