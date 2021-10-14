import re


def format_to_markdown(text):
    ''' 1. 单个换行，前置两个空格
    '''
    enter_pattern = re.compile(r'\n')
    text_formatted = ''
    last_end_index = 0
    for match in re.finditer(enter_pattern, text):
        start_index = match.start()
        end_index = match.end()

        need_space = True
        if start_index == 0 or text[start_index - 1] == '\n':
            need_space = False
        if end_index == len(text) or text[end_index] == '\n':
            need_space = False

        text_formatted += text[last_end_index:start_index]
        if need_space:
            if not text_formatted.endswith('  '):
                text_formatted += '  '
        text_formatted += '\n'
        last_end_index = end_index

    text_formatted += text[last_end_index:]

    return text_formatted
