'''Django admin configuration for bpz'''

from django.contrib.gis import admin
from .models import HomeOwnersAssociation, BOACase, TMAPCCase

geo_admin = admin.OSMGeoAdmin


class HomeOwnersAssociationAdmin(geo_admin):
    pass


class BOACaseAdmin(geo_admin):
    pass


class TMAPCCaseAdmin(geo_admin):
    pass


admin.site.register(HomeOwnersAssociation, HomeOwnersAssociationAdmin)
admin.site.register(BOACase, BOACaseAdmin)
admin.site.register(TMAPCCase, TMAPCCaseAdmin)
