from datachecker.helper.log.logger import logInfo


def run_custom_data_quality_check(args, input_file, data):
    logInfo(f'3 - Custom Data Quality Check Module :: {input_file}')
    data.drop_duplicates(keep=False)
