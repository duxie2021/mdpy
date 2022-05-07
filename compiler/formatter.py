import re
import os


def split(text, pattern):
    block_list = []
    last_end_index = 0
    for match in re.finditer(pattern, text):
        end_index = match.end()
        block_list.append(text[last_end_index:end_index])
        last_end_index = end_index
    # 末尾
    if last_end_index != len(text):
        block_list.append(text[last_end_index:])
    return block_list


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


def replace_whitespace(text):
    text_output = ''

    waterfall_pattern = re.compile(r'\n@@====[ =]*')
    line_pattern = re.compile(r'\n|^')

    block_list = split(text, waterfall_pattern)
    for block_index, block in enumerate(block_list):
        if block_index % 2 == 0:
            text_output += block
            continue

        # 按行拆分
        line_list = split(block, line_pattern)
        for line in line_list:
            whitespace_index = 0
            for whitespace_index in range(0, len(line)):
                if line[whitespace_index] != ' ':
                    break
            if whitespace_index == 0:
                text_output += line
                continue
            text_output += ' ' * whitespace_index + line[whitespace_index:]  # U+00A0

    return text_output


def format_to_markdown(text):
    ''' 遇到行首和行尾的 {}，自动添加代码范围
    '''
    text = replace_brace(text)
    ''' 遇到（waterfall 块，行首空格），用 U+00A0 代替 U+0020
    '''
    text = replace_whitespace(text)
    ''' 遇到单换行，前置两个空格
    '''
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
