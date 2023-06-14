import re


def check_if_color(txt: str):
    if re.match(r'^(([a-f]|[A-F]|\d)([a-f]|[A-F]|\d)([a-f]|[A-F]|\d))'
                r'(?:([a-f]|[A-F]|\d)([a-f]|[A-F]|\d)([a-f]|[A-F]|\d))?$', txt):
        return 'Correct HEX'
    else:
        return 'Incorrect HEX'


print(check_if_color('abc'))
print(check_if_color('ab1'))
print(check_if_color('281'))
print(check_if_color('AB123F'))
print(check_if_color('BADACE'))
print(check_if_color('SZAFKA'))
print(check_if_color('333333333333'))
print(check_if_color('3211'))