import os

from datachecker.helper.log.logger import logInfo


def listdir_full_path(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


def dir_up(path, n):
    for _ in range(n):
        path = dir_up(path.rpartition("\\")[0], 0)
    return (path)


def create_dir(path):
    if not os.path.exists(path):
        logInfo(f'Create {str(path)}')
        os.makedirs(path)