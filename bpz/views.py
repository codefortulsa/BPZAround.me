# bpz views here
from django.shortcuts import render

from rest_framework import viewsets

from .models import Case, HomeOwnersAssociation
from .serializers import CaseSerializer, HomeOwnersAssociationSerializer


class CaseViewSet(viewsets.ModelViewSet):
    model = Case
    serializer_class = CaseSerializer


class HOAViewSet(viewsets.ModelViewSet):
    model = HomeOwnersAssociation
    serializer_class = HomeOwnersAssociationSerializer


def cases(request):
    return render(request, 'bpz/cases.jinja2', {'cases': Case.objects.all()})


def hoa(request):
    return render(request, 'bpz/hoa.jinja2', 
        {'assocs': HomeOwnersAssociation.objects.all()})
