import os


workspace_path = ''
assets_folder_path = ''
assets_repository_path = ''


def set_workspace_path(in_workspace_path, in_assets_repository_path, in_assets_folder_path):
    global workspace_path
    global assets_repository_path
    global assets_folder_path
    # 绝对路径转换
    workspace_path = os.path.abspath(in_workspace_path)
    if in_assets_folder_path is None:
        assets_repository_path = workspace_path
        assets_folder_path = os.path.join(workspace_path, 'assets')
    else:
        assets_repository_path = os.path.abspath(in_assets_repository_path)
        assets_folder_path = os.path.abspath(in_assets_folder_path)
    # 路径分隔符转换
    workspace_path = workspace_path.replace('\\', '/')
    assets_repository_path = assets_repository_path.replace('\\', '/')
    assets_folder_path = assets_folder_path.replace('\\', '/')
