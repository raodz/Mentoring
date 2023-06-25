import random
import time
from threading import Thread


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


tables = []
for number in range(10):
    table = random.sample(range(1, 101), 100)
    tables.append(table)

if __name__ == "__main__":
 t0 = Thread(target=bubble_sort, args=[tables[0]])
 t1 = Thread(target=bubble_sort, args=[tables[1]])
 t2 = Thread(target=bubble_sort, args=[tables[2]])
 t3 = Thread(target=bubble_sort, args=[tables[3]])
 t4 = Thread(target=bubble_sort, args=[tables[4]])
 t5 = Thread(target=bubble_sort, args=[tables[5]])
 t6 = Thread(target=bubble_sort, args=[tables[6]])
 t7 = Thread(target=bubble_sort, args=[tables[7]])
 t8 = Thread(target=bubble_sort, args=[tables[8]])
 t9 = Thread(target=bubble_sort, args=[tables[9]])

threads = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9]

start = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end = time.time()

print('Time taken in seconds -', end - start)
