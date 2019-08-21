import re
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
import logging
import pandas as pd
import raccoon


log = logging.getLogger(__name__)


def rc_to_pd(raccoon_dataframe):
    """
    Convert a raccoon dataframe to pandas dataframe

    :param raccoon_dataframe: raccoon DataFrame
    :return: pandas DataFrame
    """
    data_dict = raccoon_dataframe.to_dict(index=False)
    return pd.DataFrame(data_dict, columns=raccoon_dataframe.columns, index=raccoon_dataframe.index)


def parse_xml(xml_path):
    tree = ElementTree.parse(xml_path)
    root: Element = tree.getroot()

    columns = ['stadsdeel_code', 'dossier_nummer', 'subdossier', 'barcode', 'scan_nr', 'file_name']

    df = raccoon.DataFrame(columns=columns)

    max_dossiers = 20
    dossier_els = root.findall('dossier')
    log.info(f'number of dossier(s): {len(dossier_els)}')

    example_cnt = 0
    for index, dossier_el in enumerate(dossier_els):  # dossier
        row_data = {
            'stadsdeel_code': dossier_el.find('stadsdeelcode').text,
            'dossier_nummer': dossier_el.find('dossierNr').text,
        }

        for sub_el in dossier_el.find('subDossiers'):
            row_data['subdossier'] = sub_el.find('titel').text

            for document_el in sub_el.find('documenten'):
                row_data['scan_nr'] = 1
                row_data['barcode'] = document_el.find('barcode').text

                bestanden_el = document_el.find('bestanden')
                url_el = bestanden_el.findall('url')[0]

                m = re.search('\/(\w+\.\w+)$', url_el.text)
                row_data['file_name'] = m.group(1)

                df.append_row(example_cnt, row_data)
                example_cnt += 1

        if index + 1 >= max_dossiers:
            log.warning(f'skipping rest, reached max_dossiers: {max_dossiers}')
            break

    df.show()

    return rc_to_pd(df)
