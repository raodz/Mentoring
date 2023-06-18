def arg_check(arg):
    def check(old_func):
        def new_func():

            pass # do sth with arg and call old_func as examp

        return new_func

    return check

arg = 'some argument'
@arg_check(arg)
def examp(num):
    pass # do sth
