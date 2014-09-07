from datetime import datetime
from json import loads
from sys import stderr
from time import mktime

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from django.db import IntegrityError
from parsedatetime import Calendar

from bpz.models import Case

'''
Import BPZ case data
'''


def _parse_datetime(value):
    calendar = Calendar()
    raw_date = loads('"%s"' % value)
    timestamp = mktime(calendar.parseDateText(raw_date))
    return datetime.fromtimestamp(timestamp).date()


def _parse_raw_value(raw_value):
    value = raw_value
    if '\r\n' in raw_value:
        stderr.write('Invalid Location %s' % repr(raw_value))
        value = raw_value.split('\r\n', 1)[0]
    return loads('"%s"' % value)


# http://stackoverflow.com/a/19357056/571420
def update_or_create(command, model, filter_kwargs, update_kwargs):
    if not model.objects.filter(**filter_kwargs).update(**update_kwargs):
        kwargs = filter_kwargs.copy()
        kwargs.update(update_kwargs)
        try:
            model.objects.create(**kwargs)
            print('New case "%s"' % kwargs['case_id'])
            command.new += 1
        except IntegrityError:
            if not (model.objects.filter(**filter_kwargs)
                    .update(**update_kwargs)):
                raise
    else:
        print('Updated case "%s"' % update_kwargs['case_id'])
        command.updated += 1


class Command(BaseCommand):
    args = '<cases.json>'
    help = 'Imports case GeoJSON'
    new, updated = 0, 0

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Pass one json file to import')

        # Load data
        datasource = DataSource(args[0], encoding='iso-8859-1')
        layer = datasource[0]
        for feature in layer:
            # Get the common attributes' values
            attr = {
                'object_id': feature['OBJECTID'].value,
                'case_id': loads('"%s"' % feature['Case_'].value),
                'status': feature['Status'].value,
                'link': loads('"%s"' % feature['Link'].value),
            }
            attr['location'] = _parse_raw_value(feature['Location'].value)
            attr['hearing_date'] = _parse_datetime(feature['Date_'].value)
            attr['geom'] = GEOSGeometry(feature.geom.wkt)

            # Get the custom attribute values: case_type & domain
            domain = Case.DOMAIN_TMAPC
            case_type = None
            if 'BOA' in attr['case_id']:
                domain = Case.DOMAIN_BOA
                case_type = Case.DOMAIN_CHOICES[domain]
            else:
                case_type = _parse_raw_value(feature['Type'].value)
            attr['case_type'] = case_type

            filter_kwargs = {'object_id': attr['object_id'],
                             'domain': domain}
            update_or_create(self, Case, filter_kwargs, attr)

        self.stdout.write(
            'Imported %d %s cases (%d new, %d updated)' %
            (self.new + self.updated, Case.DOMAIN_CHOICES[domain],
             self.new, self.updated)
        )
