from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping

from bpz.models import BOACase

'''Import Board of Adjustment cases data

TODO:
- Convert date to string
- Convert \/ in URLs
- Don't duplicate existing data
- Update existing data
'''


class Command(BaseCommand):
    args = '<home-owners-associatons.json>'
    help = 'Imports Home Owners Association GeoJSON'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Must pass exactly one json file to import')
        hoa_json = args[0]
        lm = LayerMapping(
            BOACase, hoa_json, BOACase._mapping,
            transform=False, encoding='iso-8859-1')
        lm.save(strict=False, verbose=True)
