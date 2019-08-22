# General import
import glob
import os
import pandas
import sys

import django
import logging

# Setup Django outside of `manage.py`
from pandas import DataFrame

from import_lib.stadsarchief.labels_yaml import load_labels
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "annotation_server.settings")
django.setup()

# Django specific imports
from user_model.models import AnnotationUser
from data_model.models import Example, Annotation, StringTag

# Django model dependent imports

assert len(sys.argv) == 2, f'sys.argv: {sys.argv}'

LABEL_DIR = sys.argv[1]


log_level = logging.DEBUG
root = logging.getLogger()
root.setLevel(log_level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log_level)
root.addHandler(handler)

log = logging.getLogger(__name__)


def main():
    user, created = AnnotationUser.objects.get_or_create(username='ruurd')

    if not created:
        log.info('removing all existing user annotations')
        Annotation.objects.filter(author=user).delete()

    df: pandas.DataFrame = load_labels(LABEL_DIR)

    for index, row in df.iterrows():
        examples = Example.objects.filter(reference=row['file_name'])

        if len(examples) > 0:
            example = examples[0]

            tag = StringTag.objects.create(key='type', value=row['label'])
            Annotation.objects.create(tag=tag, example=example, author=user)
            log.info(f'example: {example} annotated: {tag}')
        else:
            log.info('reference not found for label: {}')


if __name__ == "__main__":
    main()
