from json import loads

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.gdal import DataSource, OGRException

from bpz.models import HomeOwnersAssociation

'''Import Home Owners Association data

TODO: Refactor into utility function with other load_* commands
'''


class Command(BaseCommand):
    args = '<home-owners-associatons.json>'
    help = 'Imports Home Owners Association GeoJSON'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Must pass exactly one json file to import')

        same, new, updated, skipped = 0, 0, 0, 0  # Object counts

        # Load data
        datasource = DataSource(args[0], encoding='iso-8859-1')
        layer = datasource[0]
        for feature in layer:
            # Gather and transform attributes
            attr = {
                'object_id': feature['OBJECTID'].value,
                'name': loads('"%s"' % feature['Name'].value),
            }

            raw_hoa_name = feature['HOA_Name'].value
            if '\r\n' in raw_hoa_name:
                self.stderr.write('Invalid HOA_Name %s' % repr(raw_hoa_name))
                raw_hoa_name = raw_hoa_name.split('\r\n', 1)[0]
            attr['hoa_name'] = loads('"%s"' % raw_hoa_name)

            if not (attr['name'] or attr['hoa_name']):
                self.stderr.write('Unnamed HOA')
                skipped += 1
                continue

            try:
                geom = feature.geom
            except OGRException:
                self.stderr.write(
                    'No or invalid geometry for %s' % attr['name'])
                skipped += 1
                continue
            attr['geom'] = geom.wkt

            # Is there a matching HOA?
            if attr['object_id']:
                hoa_query = HomeOwnersAssociation.objects.filter(
                    object_id=attr['object_id'])
            else:
                self.stderr.write(
                    'Useless object_id %d for %s' %
                    (attr['object_id'], attr['name']))
                assert attr['name']
                hoa_query = HomeOwnersAssociation.objects.filter(
                    name=attr['name'])
            if hoa_query.exists():
                hoa = hoa_query.get()

                # Did the data change?
                different = []
                for name, new_value in attr.items():
                    existing = getattr(hoa, name)
                    if existing != new_value:
                        different.append((name, existing, new_value))
                if different:
                    updated += 1
                    diff_message = ', '.join(
                        ["%s:'%s' -> '%s'" % x for x in different])
                    msg = 'Updated HOA "%s" (%s)' % (
                        attr['name'], diff_message)
                    self.stdout.write(msg)
                else:
                    same += 1
                    self.stdout.write(
                        'No change to HOA "%s"' % attr['name'])
            else:
                # Create new HOA
                hoa = HomeOwnersAssociation()
                self.stdout.write('New HOA "%s"' % attr['name'])
                new += 1
                different = True

            if different:
                # Save changes
                for name, value in attr.items():
                    setattr(hoa, name, value)
                hoa.save()

        self.stdout.write(
            'Imported %d Home Owner Associations (%d new, %d changed,'
            ' %d unchanged, %d skipped)' %
            (new + updated + same, new, updated, same, skipped))
