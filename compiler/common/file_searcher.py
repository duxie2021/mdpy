import os
from . import file_helper
from .. import global_config


def fill_file(file):
    # 路径有效，跳过。绝对路径，相对当前目录。
    if os.path.exists(file):
        return file
    # 迭代补全
    filled = file
    config = global_config.get_config()
    for folder in config.search_file_folders:
        print(folder)
        maybe = os.path.join(folder, file)
        if os.path.exists(maybe):
            filled = maybe
            break

    filled = file_helper.normalize_file_path(filled)
    return filled
