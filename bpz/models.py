'''Models for bpz'''
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Case(models.Model):
    '''Planning or zoning case

    Model generated w/ ogrinspect. Omitted fields:
    SHAPE_Leng - derive from geometry
    SHAPE_Area - derive from geometry
    '''
    NAME_BOA = "Board of Adjustment"
    NAME_TMAPC = "Tulsa Metropolitan Area Planning Commission"
    DOMAIN_BOA = 0
    DOMAIN_TMAPC = 1
    DOMAIN_CHOICES = (
        (DOMAIN_BOA, NAME_BOA),
        (DOMAIN_TMAPC, NAME_TMAPC),
    )

    STATUS_CHOICES = [(x, x) for x in (
        'Pending',
        'Continued',
        'Approved',
        'Deny',
    )]

    CASE_TYPE_CHOICES = [(x, x) for x in (
        NAME_BOA,
        "Corridor Minor Amendment",
        "Corridor Plan",
        "Lot Split",
        "PUD Major Amendment",
        "PUD Minor Amendment",
        "PUD Site Plan",
        "PUD",
        "Subdivision Plat",
        "Zoning",
    )]

    object_id = models.IntegerField()
    case_id = models.CharField(max_length=30)
    domain = models.CharField(max_length=10, choices=DOMAIN_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=50)
    link = models.URLField()
    hearing_date = models.DateField()
    # TODO: remove choices constraint from case_type field
    case_type = models.CharField(max_length=30, choices=CASE_TYPE_CHOICES)
    geom = models.GeometryField(srid=4326)
    objects = models.GeoManager()

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

    class Meta:
        verbose_name = 'Home Owners Association'

    def __str__(self):
        return self.name or '<unnamed>'
