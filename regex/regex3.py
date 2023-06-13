import re


def check_text_structure(text: str):
    if re.search(r'[a-z]+_[a-z]+', text):
        return 'String is like abcd_efg'
    else:
        return 'String is not like abcd_efg'


print('some_text: ' + check_text_structure('some_text'))
print('some_text123: ' + check_text_structure('some_text123'))
print('some_123text: ' + check_text_structure('some_123text'))
print('Some_text: ' + check_text_structure('Some_text'))
print('Some_Text: ' + check_text_structure('Some_Text'))
