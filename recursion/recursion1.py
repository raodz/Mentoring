def show_number(lst: list, idx: int = 0):
    print(lst[idx])
    if idx == len(lst) - 1:
        return 1
    return show_number(lst, idx + 1)


numbers = list(range(15))

show_number(numbers)
