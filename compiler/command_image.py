import os
from datetime import datetime
from . import global_config
from . import file_helper
from . import statement_stack


template = '''
<!-- $${statement} -->
<img src="{relative_path}"{width_property}{height_property}>
'''


def image(path, width=None, height=None):
    # 检查文件有效
    if not os.path.exists(path):
        raise
    # 路径
    if not path.startswith(global_config.assets_folder_path):
        date_text = datetime.today().strftime('%Y%m%d')
        year_text = datetime.today().strftime('%Y')
        for i in range(1, 1_0000):
            file_name = f'{date_text}_{i:04d}' + os.path.splitext(path)[1]
            image_path = os.path.join(global_config.assets_folder_path, year_text, file_name)
            if not os.path.exists(image_path):
                break
        file_helper.force_copy(path, image_path)

    relative_path = image_path.replace(global_config.workspace_path, '').replace('\\', '/')
    if width is None:
        width_property = ''
    else:
        width_property = f' width="{width}"'
    if height is None:
        height_property = ''
    else:
        height_property = f' height="{height}"'
    return template.format(
        statement=statement_stack.peak(),
        relative_path=relative_path,
        width_property=width_property,
        height_property=height_property,
    )
