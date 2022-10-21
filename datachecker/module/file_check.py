import os

from datachecker.helper.directory.extension import listdir_full_path, create_dir
from datachecker.helper.log.logger import logWarn, logInfo
from datachecker.module.data_quality_check import run_data_quality_check


def run_file_check(args):
    create_file_check_dir(args)
    input_file_list = listdir_full_path(data_full_path(args, args.input))
    if len(input_file_list) <= 0:
        logWarn(f'- No input data to check')

    for input_file in input_file_list:
        logInfo(f'1 - File Check Module :: {input_file}')

        if check_if_file_is_already_processed(args, input_file):
            logInfo(f'File :: {input_file} already processed. Moving to next step.')
            move_file_as_processed(args, input_file)

        elif check_if_file_is_empty(input_file):
            logInfo(f"{input_file} is empty, move to unprocessed directory.")
            move_file_as_unprocessed(args, input_file)

        elif check_if_file_is_not_csv(input_file):
            logInfo(f"{input_file} is not a CSV, move to unprocessed directory.")
            move_file_as_unprocessed(args, input_file)

        else:
            run_data_quality_check(args, input_file)
            move_file_as_processed(args, input_file)


def create_file_check_dir(args):
    dir_list = [args.input, args.output, args.process, args.unprocess]
    for dir_name in dir_list:
        create_dir(data_full_path(args, dir_name))


def data_full_path(args, dir_name):
    return os.path.join(args.directory, dir_name)


def check_if_file_is_already_processed(args, input_file):
    logInfo(f'Checking, if File :: {input_file} is already processed.')
    input_file_name = os.path.basename(input_file)
    processed_file_list = listdir_full_path(data_full_path(args, args.process)) + listdir_full_path(
        data_full_path(args, args.unprocess))
    for processed_file in processed_file_list:
        processed_file_name = os.path.basename(processed_file)
        if processed_file_name == input_file_name:
            return True
        return False


def check_if_file_is_empty(input_file):
    logInfo(f'Checking, if File :: {input_file} is empty.')
    if os.stat(input_file).st_size == 0:
        return True
    return False


def move_file_as_unprocessed(args, input_file):
    unprocess_file_path = data_full_path(args, args.unprocess)
    input_file_name = os.path.basename(input_file)
    dest_file = f'{unprocess_file_path}\\{input_file_name}'
    if os.path.isfile(dest_file):
        os.remove(dest_file)
    os.rename(input_file, dest_file)


def move_file_as_processed(args, input_file):
    process_file_path = data_full_path(args, args.process)
    input_file_name = os.path.basename(input_file)
    dest_file = f'{process_file_path}\\{input_file_name}'
    if os.path.isfile(dest_file):
        os.remove(dest_file)
    os.rename(input_file, dest_file)


def check_if_file_is_not_csv(input_file):
    logInfo(f'Checking, if File :: {input_file} is not CSV.')
    input_file_name = os.path.basename(input_file)
    if not str(input_file_name).lower().endswith('.csv'):
        return True
    return False
