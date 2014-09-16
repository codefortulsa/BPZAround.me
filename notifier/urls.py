'''Views for notifier'''
from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns(
    '',
    url(r'$twiliosms&', 'notifier.views.incomingsms'),
    url(r'$update/(?P<nonce>.*)/', 'notifier.views.changesettings'),
)
