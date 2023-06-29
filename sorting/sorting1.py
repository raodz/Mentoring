import random
import time


def bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def insertion_sort(array: list):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def partition(array: list, i: int, j: int):
    pivot_idx = (i + j) // 2
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


thousand = random.sample(range(1000), 1000)
ten_thousand = random.sample(range(10000), 10000)
hundred_thousand = random.sample(range(100000), 100000)
million = random.sample(range(1000000), 1000000)

samples = [thousand, ten_thousand, hundred_thousand, million]
sort_types = [bubble_sort, insertion_sort, quick_sort]

with open('sorting_results.txt', 'w') as file:
    for sample in samples:
        file.write(f'{int(len(sample))} elements:\n\n\n')
        for sort_type in sort_types:
            start = time.time()
            sort_type(sample)
            end = time.time()
            file.write(f'{sort_type.__name__}: {end - start}\n\n')
