import re


def check_html(text: str):
    if re.match(r'(<)(\w*?)(>)(.*</)\2', text):
        return 'Correct html code'
    else:
        return 'Incorrect html code'


print('some_text: ' + check_html('some_text'))
print('some_code: ' + check_html('<some_code>Some content</some_code>'))
print('some_code_other_code: ' + check_html('<some_code>Some content</other_code>'))
print('span: ' + check_html('<span>Yowza! That’s a great regular expression.</span>'))
print('two: ' + check_html('<p>Learn about regular expressions here.</p> '
                           '<p>You\'re going to love them!</p> '))
print('two_first_ruined: ' + check_html('<p>Learn about regular expressions '
                                        'here.</p_ruined> '
                                        '<p>You\'re going to love them!</p> '))
print('two_second_ruined: ' + check_html('<p>Learn about regular expressions here.</p> '
                                         '<p>You\'re going to love them!</p_ruined> '))
# Problem z zachłannością
