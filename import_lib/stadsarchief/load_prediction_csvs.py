import csv
import glob
import logging
import sys

import raccoon

from import_lib.stadsarchief.bwt_xml import rc_to_pd

log = logging.getLogger(__name__)


def load_dir(directory):
    columns = ['file_name', 'prediction', 'confidence']

    df = raccoon.DataFrame(columns=columns)

    file_paths = glob.glob(f"{directory}/*.csv")

    if len(file_paths) == 0:
        print(f'no csv files found, {directory} exists?')

    log.info(f'loading {len(file_paths)} csv files...')

    max_predictions = sys.maxsize
    cnt = 0
    for path in file_paths:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            log.info(f'loading {path}...')

            row_idx = 0
            for row in csv_reader:
                log.debug(f'checking row {row_idx}: {row}')
                if row_idx == 0:
                    # Check if csv format is as expected
                    assert row[1] == 'stadsdeel_code', f'got: {row[1]}'
                    assert row[3] == 'file_name', f'got: {row[3]}'
                    assert row[4] == 'prediction', f'got: {row[4]}'
                    assert row[5] == 'confidence', f'got: {row[5]}'
                    row_idx += 1
                    continue

                row_data = {
                    'file_name': row[3],
                    'prediction': row[4],
                    'confidence': row[5]
                }

                df.append_row(cnt, row_data)

                row_idx += 1
                cnt += 1

                if cnt >= max_predictions:
                    log.warning(f'skipping rest, reached max_predictions: {max_predictions}')
                    break

    # df.show()

    return rc_to_pd(df)
