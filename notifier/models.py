'''Models for bpz notifications'''
from __future__ import unicode_literals

import hashlib
from datetime import datetime

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models
from django.conf import settings




@python_2_unicode_compatible
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
class ContactInfo(models.Model):
    '''Contact Email address or phone number
    To track an email address or phone number without using the auth system
    To allow user to cancel or make changes, send a URL with a nonce that is the authentication token
    Nonce is recreated each time user clicks a "Send me an access URL" request
    '''

    email = models.EmailField("User's email address")
    phoneNumber = models.CharField("Phone number for SMS", max_length=21, db_index=True)
    nonce = models.CharField("Security nonce for making changes", max_length=32, db_index=True, default=newNonce)
    emailVerified = models.BooleanField("Has the email address been verified?", default=False)
    killFlag = models.BooleanField("Do not send email to this address", default=False)
    createTimeStamp = models.DateTimeField(auto_now=True)
    lastEmailSent = models.DateTimeField(null=True)
    lastSMSSent = models.DateTimeField(null=True)
    NumSMSSentToday = models.IntegerField()  # for rate limiting

    class Meta:
        verbose_name = 'Contact information'

    def __str__(self):
        return self.email + " " + self.phoneNumber


@python_2_unicode_compatible
class Subscription(models.Model):
    '''Subscriptions

    There can be many records here associated with one contact record
    A subscription is a geographic location and a type

    '''

    SUBSCRIPTION_CHOICES = (
        ('N', 'Neighborhood association news'),
        ('A', 'Board of Adjustment notifications'),
        ('T', 'TMAP notifications'),
    )

    contactInfo = models.ForeignKey(ContactInfo)
    subscriptionType = models.CharField(max_length=1, null=False, choices=SUBSCRIPTION_CHOICES)
    geom = models.GeometryField(srid=4326)
    nextNotification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User subscription'

    def __str__(self):
        return self.PK + " " + self.subscriptionType + " " + self.nextNotification

