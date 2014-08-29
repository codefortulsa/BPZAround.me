'''Views for bpz'''
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import CaseViewSet, HOAViewSet


router = routers.DefaultRouter()
router.register(r'cases', CaseViewSet)
router.register(r'hoas', HOAViewSet)

urlpatterns = patterns(
    '',
    url(r'^$',
        TemplateView.as_view(template_name='bpz/home.jinja2'),
        name='home'),
    url(r'^about', TemplateView.as_view(
        template_name='bpz/about.jinja2'),
        name='about'),
    url(r'^api/', include(router.urls)),
)
