calls = {}
'''
Wg zadania to count() ma tworzyć słownik, ale nie wiem, jak miałyby się wtedy
zapisywać kolejne wywołania
'''

def count(function):
    def inner(*args, **kwargs):
        try:
            calls[function.__name__] += 1
        except KeyError:
            calls[function.__name__] = 1

    return inner

@count
def first_function():
    pass

@count
def second_function(some_str: str):
    return some_str

@count
def third_function(some_str: str, some_bool = True):
    if some_bool:
        return some_str

first_function()
second_function('')
second_function('')
third_function('')
third_function('', False)
third_function('', False)

print(calls)