import os


workspace_path = ''
assets_folder_path = ''


def set_workspace_path(path):
    global workspace_path
    global assets_folder_path
    workspace_path = path.replace('\\', '/')
    assets_folder_path = os.path.join(workspace_path, 'assets').replace('\\', '/')
