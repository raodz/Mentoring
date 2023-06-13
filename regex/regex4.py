import re


def check_text_end(text: str):
    if re.search(r'^.*ss$', text):
        return 'String ends with ss'
    else:
        return 'String does not end with ss'


print('ross: ' + check_text_end('ross'))
print('ros: ' + check_text_end('ros'))
print('ROSS: ' + check_text_end('ROSS'))
print('ssssssssssssssssa: ' + check_text_end('ssssssssssssssssa'))
print('ss: ' + check_text_end('ss'))
