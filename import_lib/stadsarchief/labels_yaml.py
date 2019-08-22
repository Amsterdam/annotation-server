import glob
import logging
import sys

import raccoon
import yaml

from import_lib.stadsarchief.bwt_xml import rc_to_pd


log = logging.getLogger(__name__)


def load_yaml(path):
    with open(path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return data


def load_labels(label_dir):
    columns = ['file_name', 'label']

    df = raccoon.DataFrame(columns=columns)

    file_paths = glob.glob(f"{label_dir}/*.yaml")

    if len(file_paths) == 0:
        print(f'no labels found, {label_dir} exists?')

    file_paths_sorted = sorted(file_paths)

    log.info(f'loading {len(file_paths_sorted)} yaml files...')

    max_labels = sys.maxsize
    cnt = 0
    for path in file_paths_sorted:
        data = load_yaml(path)

        row_data = {
            'file_name': data.get('reference'),
            'label': data.get('type'),
        }

        df.append_row(cnt, row_data)

        cnt += 1

        if cnt >= max_labels:
            log.warning(f'skipping rest, reached max_labels: {max_labels}')
            break


    df.show()

    return rc_to_pd(df)
