from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping

from bpz.models import HomeOwnersAssociation

'''Import Home Owners Association data

TODO:
- Don't duplicate existing data
- Exclude data with object_id = 0?
- Import neighborhoods with no geometry?
- Handle names with \/
- strict = True?
'''


class Command(BaseCommand):
    args = '<home-owners-associatons.json>'
    help = 'Imports Home Owners Association GeoJSON'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Must pass exactly one json file to import')
        hoa_json = args[0]
        lm = LayerMapping(
            HomeOwnersAssociation, hoa_json, HomeOwnersAssociation._mapping,
            transform=False, encoding='utf-8')
        lm.save(strict=False, verbose=True)
