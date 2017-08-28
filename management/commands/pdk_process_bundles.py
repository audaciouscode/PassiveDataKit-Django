# pylint: disable=no-member,line-too-long

import datetime
import json
import logging

from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand
from django.utils import timezone

from ...decorators import handle_lock
from ...models import DataServerMetadatum, DataPoint, DataBundle, install_supports_jsonfield, \
                      TOTAL_DATA_POINT_COUNT_DATUM, SOURCES_DATUM, SOURCE_GENERATORS_DATUM

class Command(BaseCommand):
    help = 'Convert unprocessed DataBundle instances into DataPoint instances.'

    def add_arguments(self, parser):
        parser.add_argument('--delete',
                            action='store_true',
                            dest='delete',
                            default=False,
                            help='Delete data bundles after processing')

        parser.add_argument('--count',
                            type=int,
                            dest='bundle_count',
                            default=25,
                            help='Number of bundles to process in a single run')

    @handle_lock
    def handle(self, *args, **options): # pylint: disable=too-many-locals, too-many-branches, too-many-statements
        to_delete = []

        supports_json = install_supports_jsonfield()
        default_tz = timezone.get_default_timezone()

        new_point_count = 0

        seen_sources = []
        source_identifiers = {}

        for bundle in DataBundle.objects.filter(processed=False).order_by('-recorded')[:options['bundle_count']]:
            if supports_json is False:
                bundle.properties = json.loads(bundle.properties)

            for bundle_point in bundle.properties:
                if 'passive-data-metadata' in bundle_point:
                    point = DataPoint(recorded=timezone.now())
                    point.source = bundle_point['passive-data-metadata']['source']
                    point.generator = bundle_point['passive-data-metadata']['generator']

                    if 'generator-id' in bundle_point['passive-data-metadata']:
                        point.generator_identifier = bundle_point['passive-data-metadata']['generator-id']

                    if 'latitude' in bundle_point['passive-data-metadata'] and 'longitude' in bundle_point['passive-data-metadata']:
                        point.generated_at = GEOSGeometry('POINT(' + str(bundle_point['passive-data-metadata']['longitude']) + ' ' + str(bundle_point['passive-data-metadata']['latitude']) + ')')

                    point.created = datetime.datetime.fromtimestamp(bundle_point['passive-data-metadata']['timestamp'], tz=default_tz)

                    if supports_json:
                        point.properties = bundle_point
                    else:
                        point.properties = json.dumps(bundle_point, indent=2)

                    point.fetch_secondary_identifier()

                    point.save()

                    if (point.source in seen_sources) is False:
                        seen_sources.append(point.source)

                    if point.source in source_identifiers:
                        source_identifiers = source_identifiers[point.source]

                    new_point_count += 1

            bundle.processed = True
            bundle.save()

            if options['delete']:
                to_delete.append(bundle)

        for bundle in to_delete:
            bundle.delete()

        data_point_count = DataServerMetadatum.objects.filter(key=TOTAL_DATA_POINT_COUNT_DATUM).first()

        if data_point_count is None:
            count = DataPoint.objects.all().count()

            data_point_count = DataServerMetadatum(key=TOTAL_DATA_POINT_COUNT_DATUM)

            data_point_count.value = str(count)
            data_point_count.save()
        else:
            count = int(data_point_count.value)

            count += new_point_count

            data_point_count.value = str(count)
            data_point_count.save()

        data_point_count = DataServerMetadatum.objects.filter(key=TOTAL_DATA_POINT_COUNT_DATUM).first()

        sources = DataServerMetadatum.objects.filter(key=SOURCES_DATUM).first()

        if sources is not None:
            updated = False

            source_list = json.loads(sources.value)

            for seen_source in seen_sources:
                if (seen_source in source_list) is False:
                    source_list.append(seen_source)

                    updated = True

            if updated:
                sources.value = json.dumps(source_list, indent=2)
                sources.save()
        else:
            DataPoint.objects.sources()

        for source, identifiers in source_identifiers.iteritems():
            datum_key = SOURCE_GENERATORS_DATUM + ': ' + source
            source_id_datum = DataServerMetadatum.objects.filter(key=datum_key).first()

            source_ids = []

            if source_id_datum is not None:
                source_ids = json.loads(source_id_datum.value)
            else:
                source_id_datum = DataServerMetadatum(key=datum_key)

            updated = False

            for identifier in identifiers:
                if (identifier in source_ids) is False:
                    source_ids.append(identifier)

                    updated = True

            if updated:
                source_id_datum.value = json.dumps(source_ids, indent=2)
                source_id_datum.save()

        logging.debug("%d unprocessed payloads remaining.", DataBundle.objects.filter(processed=False).count())
