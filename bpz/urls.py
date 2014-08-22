'''Views for bpz'''
from django.conf.urls import patterns, url

from .views import RequestView

urlpatterns = patterns(
    '',
    url(r'^$', RequestView.as_view(
        template_name='bpz/home.jinja2'),
        name='home'),
)
