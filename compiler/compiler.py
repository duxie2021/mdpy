''' 整理markdownw文档中的图片
    1. 把非 assets 目录的文件移动到 assets 目录，并且按照年份归档
'''
import os
import re
from . import global_config
from . import formatter
from . import statement_stack
from .command_image import image


def compile_one_file(file_path):
    # read file
    print(f'compile file[{file_path}]')
    with open(file_path, encoding='utf8') as f:
        file_origin = f.read()

    file_generated = ''
    match_end_index = 0
    # 暂时只支持单行，多行要上词法分析器
    command_pattern = re.compile(r'\n\$\$(.*)\n')
    for match in re.finditer(command_pattern, file_origin):
        statement = match.group(1)
        statement = statement.replace('\\', '/')
        statement_stack.push(statement)
        generated_text = eval(statement)
        statement_stack.pop(statement)
        file_generated += file_origin[match_end_index:match.start()] + generated_text
        match_end_index = match.end()

    file_generated += file_origin[match_end_index:]
    file_formatted = formatter.format_to_markdown(file_generated)
    # write file
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(file_formatted)


def compile(workspace_path):
    global_config.set_workspace_path(workspace_path)

    for path, folders, files in os.walk(workspace_path):
        for file in files:
            if not file.endswith('.md'):
                continue

            file_path = os.path.join(path, file)
            compile_one_file(file_path)
