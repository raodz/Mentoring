import time


def timethis(function):
    def inner(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        stop = time.time()
        duration = stop - start
        print(duration)

    return inner


'''Tests'''


@timethis
def first_function():
    for number in range(500):
        pass


@timethis
def second_function(some_str: str):
    for number in range(1000):
        some_str += 'a'
    return some_str


@timethis
def third_function(some_str: str, some_bool=False):
    if some_bool:
        for number in range(1500):
            some_str += 'a'
        return some_str


first_function()
second_function('')
third_function('', True)
