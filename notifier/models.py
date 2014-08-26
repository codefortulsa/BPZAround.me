'''Models for bpz notifications'''
from __future__ import unicode_literals

import hashlib
from datetime import datetime

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models
from django.conf import settings


def newNonce(self=None):
    '''
    create a new nonce using md5, the secret key, current timestamp and optionally a primary key
    :param self:
    :return nonce:
    '''

    if self is not None:
        hashsrc = '%s%s%s' % (self.pk, settings.SECRET_KEY, datetime.utcnow())
        nonce = hashlib.md5(hashsrc).hexdigest()
    else:
        hashsrc = '%s%s' % (settings.SECRET_KEY, datetime.utcnow())
        nonce = hashlib.md5(hashsrc).hexdigest()
    return nonce


@python_2_unicode_compatible
class NotificationEmail(models.Model):
    '''Notification Email
    To track an email without using the auth system
    To allow user to cancel or make changes, send a URL with a nonce that is the authentication token
    Nonce is recreated each time user clicks a "Send me an access URL" request
    '''

    email = models.EmailField("User's email address")
    nonce = models.CharField("Security nonce for making changes", max_length=32, db_index=True, default=newNonce)
    emailVerified = models.BooleanField("Has the email address been verified?", default=False)
    killFlag = models.BooleanField("Do not send email to this address", default=False)
    createTimeStamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Notification Emails'

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class NotificationPhone(models.Model):
    '''Notification phone number
    To track a phone number without using the auth system
    To allow user to cancel or make changes, send a URL with a nonce that is the authentication token
    Nonce is recreated each time user clicks a "Send me an access URL" request
    Also, the user can do some things by replying
    '''

    # TODO: create a view for the incoming twilio SMS request (and a static one for phone calls)

    phoneNumber = models.CharField("Phone number for SMS", max_length=21, db_index=True)
    nonce = models.CharField("Security nonce for making changes", max_length=32, db_index=True, default=newNonce)
    emailVerified = models.BooleanField("Has the phone number been verified?", default=False)
    killFlag = models.BooleanField("Do not send text messages to this phone", default=False)
    createTimeStamp = models.DateTimeField("Record create date / time", auto_now=True)

    class Meta:
        verbose_name = 'Notification Emails'

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class Subscription(models.Model):
    '''Subscriptions

    There can be many records here associated with one email and / or phone
    A subscription is a geographic location and a type

    '''

    SUBSCRIPTION_CHOICES = (
        ('N', 'Neighborhood association news'),
        ('A', 'Board of Adjustment notifications'),
        ('T', 'TMAP (?) notifications'),
    )

    notifyEmail = models.ForeignKey(NotificationEmail)
    notifyPhone = models.ForeignKey(NotificationPhone)
    subscriptionType = models.CharField(max_length=1, null=False, choices=SUBSCRIPTION_CHOICES)
    geom = models.GeometryField(srid=4326)
    lastEmailSent = models.DateTimeField(null=True)
    lastSMSSent = models.DateTimeField(null=True)
    textsSentToday = models.IntegerField()

