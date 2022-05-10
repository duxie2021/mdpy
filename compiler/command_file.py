import os
from datetime import datetime
from . import global_config
from . import statement_stack
from .common import file_helper
from .common import file_searcher


template = '''
<!-- $${statement} -->
<a href="{relative_path}">{description}</a>
'''


def file(path, description=None):
    if description is None:
        description = os.path.basename(path)

    # 搜索文件路径
    path = file_searcher.fill_file(path)
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

    relative_path = image_path.replace(global_config.assets_repository_path, '').replace('\\', '/')
    return template.format(
        statement=statement_stack.peak(),
        relative_path=relative_path,
        description=description,
    )
