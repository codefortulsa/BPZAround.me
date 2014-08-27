'''Django admin configuration for bpz'''

from django.contrib.gis import admin
from .models import Case, HomeOwnersAssociation

geo_admin = admin.OSMGeoAdmin


class HomeOwnersAssociationAdmin(geo_admin):
    pass


class CaseAdmin(geo_admin):
    pass


admin.site.register(Case, CaseAdmin)
admin.site.register(HomeOwnersAssociation, HomeOwnersAssociationAdmin)
