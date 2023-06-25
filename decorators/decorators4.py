def arg_check(arg):
    def check(old_func):
        def new_func(*args):

            if isinstance(*args, arg):
                print("Types are the same")
            else:
                print('Tncorrect types')

        return new_func

    return check


arg = 'some argument'


@arg_check(arg)
def examp(num: int):
    return num + 1


examp(5)

