def show_number(num: int):
    print(num)
    if num == 0:
        return 1
    return show_number(num - 1)


show_number(15)
