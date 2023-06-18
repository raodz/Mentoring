def logged(function):
    def inner(*args):
        return f'you called {function.__name__}{args} it returned {function(*args)}'

    return inner


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
