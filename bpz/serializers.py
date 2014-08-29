from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Case, HomeOwnersAssociation


class CaseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Case
        geo_field = 'geom'
        fields = (
            'id', 'object_id', 'case_id', 'domain', 'status', 'location',
            'link', 'hearing_date', 'case_type', 'geom')


class HomeOwnersAssociationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HomeOwnersAssociation
        geo_field = 'geom'
        fields = ('id', 'object_id', 'name', 'hoa_name', 'geom')
