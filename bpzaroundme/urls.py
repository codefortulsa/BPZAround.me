from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('bpz.urls', namespace='bpz')),
    url(r'^admin/', include(admin.site.urls)),
)
