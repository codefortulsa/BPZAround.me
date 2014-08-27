'''Views for bpz'''
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import CaseViewSet, HOAViewSet


router = routers.DefaulRouter()
router.register(r'cases', CaseViewSet)
router.register(r'hoas', HOAViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^$',
        TemplateView.as_view(template_name='bpz/home.jinja2'),
        name='home'),
)
