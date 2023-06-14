import re


def get_only_numbers(txt: str):
    txt_num_only = re.sub(r'\D', '', txt)
    parts = list(txt_num_only)
    return parts


print(get_only_numbers('2 cats and 3 dogs'))
