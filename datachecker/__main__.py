import argparse
import os
import sys

from datachecker.helper.directory.extension import dir_up
from datachecker.helper.log.logger import logError
from datachecker.module.file_check import run_file_check


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='Enter the directory name')
    parser.add_argument('-o', '--output', help='Enter the output directory name', default='output')
    parser.add_argument('-i', '--input', help='Enter the input directory name', default='input')
    parser.add_argument('-p', '--process', help='Enter the process directory name', default='process')
    parser.add_argument('-u', '--unprocess', help='Enter the unprocess directory name', default='unprocess')
    args = parser.parse_args()
    args.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    args.DATA_DIR = os.path.join(dir_up(args.ROOT_DIR, 1), 'data')
    args.CONFIG_PATH = os.path.join(args.ROOT_DIR, 'configuration.conf')
    if not args.directory:
        args.directory = str(args.DATA_DIR)
    run_file_check(args)


if __name__ == '__main__':
    try:
        main()
    except:
        e = sys.exc_info()[0]
        logError(f'An exception occurred :: {e}')
