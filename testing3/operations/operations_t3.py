def partition(array: list, i: int, j: int):
    pivot_idx = i + j // 2
    pivot = array[pivot_idx]

    while i <= j:
        while pivot > array[i]:
            i += 1
        while pivot < array[j]:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    return i


def quick_sort(array: list, start: int = 0, end: int = -1):
    if end == -1:
        end = len(array) - 1
    edge = partition(array, start, end)
    if start < edge - 1:
        quick_sort(array, start, edge - 1)
    if end > edge:
        quick_sort(array, edge, end)

print(quick_sort([5, 2, 7, 1, -2, 4, 7, 4, 9, 0]))