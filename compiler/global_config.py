import os


workspace_path = ''
assets_folder_path = ''


def set_workspace_path(path):
    global workspace_path
    global assets_folder_path
    # 绝对路径转换
    workspace_path = os.path.abspath(path)
    assets_folder_path = os.path.join(workspace_path, 'assets')
    # 路径分隔符转换
    workspace_path = workspace_path.replace('\\', '/')
    assets_folder_path = assets_folder_path.replace('\\', '/')
