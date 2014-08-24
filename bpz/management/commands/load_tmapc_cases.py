from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping

from bpz.models import TMAPCCase

'''Import Tulsa Metropolitan Area Planning Commission case data

TODO:
- Convert date to string
- Convert \/ in URLs
- Don't duplicate existing data
- Update existing data
- Limit / validate case types? ('PUD Site Plan\r\n\r\nPUD Site Plan')
'''


class Command(BaseCommand):
    args = '<home-owners-associatons.json>'
    help = 'Imports Home Owners Association GeoJSON'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Must pass exactly one json file to import')
        hoa_json = args[0]
        lm = LayerMapping(
            TMAPCCase, hoa_json, TMAPCCase._mapping,
            transform=False, encoding='iso-8859-1')
        lm.save(strict=True, verbose=True)
