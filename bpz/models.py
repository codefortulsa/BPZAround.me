'''Models for bpz'''
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BOACase(models.Model):
    '''Board of Adjustment Case

    Model generated w/ ogrinspect. Omitted fields:
    SHAPE_Leng - derive from geometry
    SHAPE_Area - derive from geometry
    '''

    object_id = models.IntegerField()
    case_id = models.CharField(max_length=15)
    status = models.CharField(
        max_length=10, choices=[(x, x) for x in (
            'Pending', 'Continued', 'Approved', 'Deny')])
    location = models.CharField(max_length=50)
    link = models.URLField()
    hearing_date_str = models.CharField(max_length=15)
    geom = models.GeometryField(srid=4326)
    objects = models.GeoManager()

    _mapping = {
        'object_id': 'OBJECTID',
        'case_id': 'Case_',
        'status': 'Status',
        'location': 'Location',
        'link': 'Link',
        'hearing_date_str': 'Date_',
        'geom': 'UNKNOWN',
    }

    class Meta:
        verbose_name = 'BOA Case'

    def __str__(self):
        return self.case_id


@python_2_unicode_compatible
class HomeOwnersAssociation(models.Model):
    '''Home Owners Association

    Model generated w/ ogrinspect. Omitted fields:
    Id - Always 0
    Umbrella - 'N' or null
    Shape_Leng - derive from geometry
    Spape_Area - derive from geometry
    '''

    object_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50)
    hoa_name = models.CharField(max_length=50)
    geom = models.GeometryField(srid=4326)
    objects = models.GeoManager()

    _mapping = {
        'object_id': 'OBJECTID',
        'name': 'Name',
        'hoa_name': 'HOA_Name',
        'geom': 'UNKNOWN',
    }

    class Meta:
        verbose_name = 'Home Owners Association'

    def __str__(self):
        return self.name or '<unnamed>'


@python_2_unicode_compatible
class TMAPCCase(models.Model):
    '''Tulsa Metropolitan Area Planning Commission Case

    Model generated w/ ogrinspect. Omitted fields:
    SHAPE_Leng - derive from geometry
    SHAPE_Area - derive from geometry
    '''

    object_id = models.IntegerField()
    case_id = models.CharField(max_length=50)
    status = models.CharField(
        max_length=10, choices=[(x, x) for x in (
            'Pending', 'Continued', 'Approved', 'Deny')])
    location = models.CharField(max_length=50)
    link = models.URLField()
    case_type = models.CharField(max_length=30)
    hearing_date_str = models.CharField(max_length=15)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    _mapping = {
        'object_id': 'OBJECTID',
        'case_id': 'Case_',
        'status': 'Status',
        'location': 'Location',
        'link': 'Link',
        'case_type': 'Type',
        'hearing_date_str': 'Date_',
        'geom': 'MULTIPOLYGON',
    }

    class Meta:
        verbose_name = 'TMAPC Case'

    def __str__(self):
        return self.case_id
