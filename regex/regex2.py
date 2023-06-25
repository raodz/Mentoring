import re


def check_text_start(text: str):
    if re.match(r'^b\w*$|^0\w*$', text):
        return 'String starts with b or 0'
    else:
        return 'String starts neither with b nor 0'


print('SomeText123: ' + check_text_start('SomeText123'))
print('0SomeText123: ' + check_text_start('0SomeText123'))
print('bSomeText123: ' + check_text_start('bSomeText123'))
