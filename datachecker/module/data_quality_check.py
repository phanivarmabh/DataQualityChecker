import os

import pandas as pd

from datachecker.helper.log.logger import logInfo
from datachecker.module.custom_data_quality_checker import run_custom_data_quality_check


def run_data_quality_check(args, input_file):
    logInfo(f'2 - Data Quality Check Module :: {input_file}')
    input_file_name = os.path.basename(input_file)
    data = pd.read_csv(input_file)
    replace_whitespaces(data, 'phone')
    remove_starts_with(data, 'phone')
    remove_special_chars(data, ['address', 'reviews_list'])
    data.dropna(inplace=True)
    run_custom_data_quality_check(args, input_file, data)
    output_file_path = os.path.join(args.directory, args.output, input_file_name)
    if os.path.isfile(output_file_path):
        os.remove(output_file_path)
    data.to_csv(output_file_path, na_rep='', index=False)


def replace_whitespaces(data, col):
    data[col] = data[col].str.strip().str.replace(' ', '')


def remove_starts_with(data, col):
    data[col] = data[col].str.replace('\+', '', regex=True)


def remove_special_chars(data, cols):
    for col in cols:
        data[col] = data[col].str.replace('[@_!#$%^&*()<>?/|}{~:]', '', regex=True)
