import re
import os


def insert_h1(text, file_path):
    if text.startswith('#'):
        return text

    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]
    return f'# {file_name_without_ext}\n' + text


def replace_brace(text):
    text = re.sub(r'(?<!```)\n{\n', '\n```\n{\n', text)
    text = re.sub(r'\n}\n(?!```)', '\n}\n```\n', text)
    return text


def format_to_markdown(text):
    ''' 1. 单个换行，前置两个空格
    '''
    text = replace_brace(text)

    enter_pattern = re.compile(r'\n')
    text_formatted = ''
    last_end_index = 0
    for match in re.finditer(enter_pattern, text):
        start_index = match.start()
        end_index = match.end()

        need_space = True
        while True:
            ''' 规则1：开头，结尾，两个连续的换行 '''
            if start_index == 0 or text[start_index - 1] == '\n':
                need_space = False
                break
            if end_index == len(text) or text[end_index] == '\n':
                need_space = False
                break
            ''' 规则2：">"结尾 '''
            if text[start_index - 1] == '>':
                need_space = False
                break
            break

        text_formatted += text[last_end_index:start_index]
        if need_space:
            if not text_formatted.endswith('  '):
                text_formatted += '  '
        text_formatted += '\n'
        last_end_index = end_index

    text_formatted += text[last_end_index:]

    return text_formatted
