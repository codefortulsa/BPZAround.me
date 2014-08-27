from rest_framework import viewsets

from .models import Case, HomeOwnersAssocation


class CaseViewSet(viewsets.ModelViewSet):
    model = Case


class HOAViewSet(viewsets.ModelViewSet):
    model = HomeOwnersAssocation
