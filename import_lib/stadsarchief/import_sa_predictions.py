# General import
import logging
import os
import sys

import django
import pandas

# Setup Django outside of `manage.py`
from import_lib.stadsarchief.load_prediction_csvs import load_dir

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "annotation_server.settings")
django.setup()

# Django specific imports
from user_model.models import AnnotationUser
from data_model.models import Example, Annotation, StringTag

# Django model dependent imports

assert len(sys.argv) == 2, f'sys.argv: {sys.argv}'

PREDICTIONS_DIR = sys.argv[1]

log_level = logging.INFO
root = logging.getLogger()
root.setLevel(log_level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log_level)
root.addHandler(handler)

log = logging.getLogger(__name__)


def main():
    user, created = AnnotationUser.objects.get_or_create(username='AI')

    if not created:
        log.info('removing all existing AI annotations')
        Annotation.objects.filter(author=user).delete()

    df: pandas.DataFrame = load_dir(PREDICTIONS_DIR)

    log.info('dataframe: ')
    log.info(df)

    for index, row in df.iterrows():
        examples = Example.objects.filter(reference=row['file_name'])

        if len(examples) > 0:
            example = examples[0]

            tag = StringTag.objects.create(key='type', value=row['prediction'])
            Annotation.objects.create(tag=tag, example=example, author=user)

            tag = StringTag.objects.create(key='confidence', value=row['confidence'])
            Annotation.objects.create(tag=tag, example=example, author=user)

            log.info(f'example: {example} annotated: {tag}')
        else:
            log.info(f'reference not found for example: {row["file_name"]}')


if __name__ == "__main__":
    main()
