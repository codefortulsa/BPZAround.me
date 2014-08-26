from datetime import datetime
from json import loads
from time import mktime

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from parsedatetime import Calendar

from bpz.models import Case

'''Import Board of Adjustment cases data

TODO: Refactor into utility function with other load_* commands
'''


class Command(BaseCommand):
    args = '<boa-cases.json>'
    help = 'Imports Board of Adjustment cases GeoJSON'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Must pass exactly one json file to import')

        same, new, updated = 0, 0, 0  # Object counts
        calendar = Calendar()  # date parser

        # Load data
        datasource = DataSource(args[0], encoding='iso-8859-1')
        layer = datasource[0]
        for feature in layer:
            # Gather and transform attributes
            attr = {
                'object_id': feature['OBJECTID'].value,
                'case_id': loads('"%s"' % feature['Case_'].value),
                'status': feature['Status'].value,
                'location': loads('"%s"' % feature['Location'].value),
                'link': loads('"%s"' % feature['Link'].value),
            }

            raw_date = loads('"%s"' % feature['Date_'].value)
            timestamp = mktime(calendar.parseDateText(raw_date))
            attr['hearing_date'] = datetime.fromtimestamp(timestamp).date()

            attr['geom'] = GEOSGeometry(feature.geom.wkt)

            # Is there a case with this object ID?
            case_query = Case.objects.filter(
                object_id=attr['object_id'], domain=Case.DOMAIN_BOA)
            if case_query.exists():
                case = case_query.get()

                # Did the data change?
                different = []
                for name, new_value in attr.items():
                    existing = getattr(case, name)
                    if existing != new_value:
                        different.append((name, existing, new_value))
                if different:
                    updated += 1
                    diff_message = ', '.join(
                        ["%s:'%s' -> '%s'" % x for x in different])
                    msg = 'Updated case "%s" (%s)' % (
                        attr['case_id'], diff_message)
                    self.stdout.write(msg)
                else:
                    same += 1
                    self.stdout.write(
                        'No change to case "%s"' % attr['case_id'])
            else:
                # Create new Case
                case = Case(
                    object_id=attr['object_id'], domain=Case.DOMAIN_BOA,
                    case_type="Board of Adjustment")
                self.stdout.write('New case "%s"' % attr['case_id'])
                new += 1
                different = True

            if different:
                # Save changes
                for name, value in attr.items():
                    setattr(case, name, value)
                case.save()

        self.stdout.write(
            'Imported %d BOA cases (%d new, %d changed, %d unchanged)' % (
                new + updated + same, new, updated, same))
