import re


def check_text_structure(text: str):
    if re.match(r'[^aA]{6,}', text):
        '''Blokowanie aA nie działa - nie widzę dlaczego'''
        return 'String contains 6 chars or more and none of them is a nor A'
    else:
        return 'String contains less than 6 chars or some of them is a or A'


print('some_text: ' + check_text_structure('some_text'))
print('any_text: ' + check_text_structure('any_text'))
print('nope: ' + check_text_structure('nope'))
print('SOME_TEXT: ' + check_text_structure('SOME_TEXT'))
print('ANY_TEXT: ' + check_text_structure('ANY_TEXT'))
