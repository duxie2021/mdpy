import os
from .common import file_helper
from .common import json_helper


workspace_path = ''
assets_folder_path = ''
assets_repository_path = ''


def set_workspace_path(in_workspace_path, in_assets_repository_path, in_assets_folder_path):
    global workspace_path
    global assets_repository_path
    global assets_folder_path
    # 绝对路径转换
    workspace_path = file_helper.normalize_file_path(in_workspace_path)
    if in_assets_folder_path is None:
        assets_repository_path = workspace_path
        assets_folder_path = os.path.join(workspace_path, 'assets')
    else:
        assets_repository_path = os.path.abspath(in_assets_repository_path)
        assets_folder_path = os.path.abspath(in_assets_folder_path)
    # 路径分隔符转换
    workspace_path = file_helper.normalize_file_path(workspace_path)
    assets_repository_path = file_helper.normalize_file_path(assets_repository_path)
    assets_folder_path = file_helper.normalize_file_path(assets_folder_path)


class DefaultConfig(json_helper.EmptyConfig):

    def __init__(self):
        self.search_file_folders = []


global_config = None


def get_config():
    global global_config
    if global_config is None:
        global_config = DefaultConfig()
        global_config.load(f'{assets_repository_path}/.mdpy/config')

    return global_config
