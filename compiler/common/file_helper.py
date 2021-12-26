import os
import shutil
import re


def normalize_file_path(file_path):
    normalized = os.path.abspath(file_path)
    normalized = normalized.replace('\\', '/')
    while len(normalized) > 1 and normalized.endswith('/'):
        normalized = normalized[0:-1]
    return normalized


def force_remove(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)


def force_copy(source, dest):
    force_remove(dest)

    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))

    if os.path.isdir(source):
        shutil.copytree(source, dest)
    elif os.path.isfile(source):
        shutil.copyfile(source, dest)


def make_sure_file_path_exists(path):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def make_sure_folder_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def batch_remove_files(folder, pattern):
    for file in os.listdir(folder):
        if not os.path.isfile(file):
            continue
        if not re.match(pattern, file):
            continue

        force_remove(os.path.join(folder, file))
