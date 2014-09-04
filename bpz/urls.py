'''Views for bpz'''
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import CaseViewSet, HOAViewSet, cases, hoa


router = routers.DefaultRouter()
router.register(r'cases', CaseViewSet)
router.register(r'hoas', HOAViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^$',
        TemplateView.as_view(template_name='bpz/home.jinja2'),
        name='home'),
    url(r'^about',
        TemplateView.as_view(template_name='bpz/about.jinja2'),
        name='about'),
    url(r'^hood',
        TemplateView.as_view(template_name='bpz/hood.jinja2'),
        name='neighborhood'),
    url(r'^notify',
        TemplateView.as_view(template_name='bpz/notify.jinja2'),
        name='notify'),
    url(r'^cases', cases, name='cases'),
    url(r'^hoa', hoa, name='home_owners'),

)
