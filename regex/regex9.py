import re


def check_format_correctness(number: str):
    '''Zadanie wymaga, żeby liczba była stringiem'''
    if re.search(r'^(-?\d+)(?:,\d+)?$', number):
        return 'Number format is correct'
    else:
        return 'Number format is incorrect'

print(check_format_correctness('1'))
print(check_format_correctness('10'))
print(check_format_correctness('-10'))
print(check_format_correctness('-10,01'))
print(check_format_correctness('-10,'))
print(check_format_correctness('-'))
print(check_format_correctness('10-1'))