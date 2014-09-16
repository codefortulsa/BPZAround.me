from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('bpz.urls', namespace='bpz')),
    url(r'^', include('notifier.urls', namespace='notifier')),
    url(r'^admin/', include(admin.site.urls)),
)
