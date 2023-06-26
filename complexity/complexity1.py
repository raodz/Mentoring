def bin_search(searched_value: int, values: list):
    left = 0
    right = len(values) - 1
    while left <= right:
        mid = (left + right) // 2
        if values[mid] < searched_value:
            left = mid + 1
        elif values[mid] > searched_value:
            right = mid - 1
        else:
            return mid
    return 'Not found'

numbers = range(0, 30)

searched_idx = bin_search(20, numbers)

more_than_20 = numbers[searched_idx + 1:]

if len(more_than_20) >= 10:
    print('There is at least 10 numbers higher than 20 in this list')
else:
    print('There is less than 10 numbers higher than 20 in this list')