import re


def check_text_content(text: str):
    if re.match(r'^\w*$', text):
        return 'String contains only A-z or 0-9'
    else:
        return 'String does not contain only A-z or 0-9'


print('SomeText123: ' + check_text_content('SomeText123'))
print('Some Text 1, 2, 3: ' + check_text_content('Some Text 1, 2, 3'))
