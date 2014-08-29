from rest_framework import viewsets

from .models import Case, HomeOwnersAssociation


class CaseViewSet(viewsets.ModelViewSet):
    model = Case


class HOAViewSet(viewsets.ModelViewSet):
    model = HomeOwnersAssociation
