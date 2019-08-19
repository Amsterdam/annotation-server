# General import
import os
import sys
import urllib

import django
import logging

# Setup Django outside of `manage.py`
from pandas import DataFrame

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "annotation_server.settings")
django.setup()

# Django specific imports
from data_model.models import Example, TextFeature, Annotation, DataSource, ImageFeature, \
    StringTag

# Django model dependent imports
from import_lib.stadsarchief.bwt_xml import parse_xml

IIIF_API_ROOT = os.getenv("IIIF_API_ROOT")
assert IIIF_API_ROOT is not None

assert len(sys.argv) == 2, f'sys.argv: {sys.argv}'

XML_FILE = sys.argv[1]


log_level = logging.DEBUG
root = logging.getLogger()
root.setLevel(log_level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log_level)
root.addHandler(handler)

log = logging.getLogger(__name__)


def get_url(api_root, stadsdeel_code, dossier_nummer, filename, dim=(800, 800)):
    basename, ext = os.path.splitext(filename)
    document_part = f'{stadsdeel_code}/{str(dossier_nummer).zfill(5)}/{basename}{ext.lower()}'
    document_encoded = urllib.parse.quote_plus(document_part)
    url = f'{api_root}{document_encoded}/full/{dim[0]},{dim[1]}/0/default.jpg'
    return url


def main():
    data_source, _ = DataSource.objects.get_or_create(name='BWT')

    xml_path = XML_FILE
    log.info(f'opening {xml_path}')
    df: DataFrame = parse_xml(xml_path)

    Example.objects.filter(data_source=data_source).delete()

    for index, row in df.iterrows():
        example = Example(reference=row['file_name'], description='dossier.sub_dossier.document.bestand', data_source=data_source)
        example.save()

        url = get_url(IIIF_API_ROOT, row['stadsdeel_code'], row['dossier_nummer'], row['file_name'])

        image = ImageFeature(remote_url=url)
        image.example = example
        image.save()

        tag = StringTag.objects.create(key='stadsdeel_code', value=row['stadsdeel_code'])
        Annotation.objects.create(tag=tag, example=example)
        tag = StringTag.objects.create(key='dossier_nummer', value=row['dossier_nummer'])
        Annotation.objects.create(tag=tag, example=example)
        tag = StringTag.objects.create(key='subdossier', value=row['subdossier'])
        Annotation.objects.create(tag=tag, example=example)
        tag = StringTag.objects.create(key='barcode', value=row['barcode'])
        Annotation.objects.create(tag=tag, example=example)
        tag = StringTag.objects.create(key='scan_nr', value=row['scan_nr'])
        Annotation.objects.create(tag=tag, example=example)
        tag = StringTag.objects.create(key='file_name', value=row['file_name'])
        Annotation.objects.create(tag=tag, example=example)


if __name__ == "__main__":
    main()
