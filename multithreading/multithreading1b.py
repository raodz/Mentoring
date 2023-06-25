import random
import time
from multiprocessing import Pool


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

if __name__ == '__main__':
   pool = Pool(processes=10)
   start = time.time()
   p0 = pool.apply_async(bubble_sort, [tables[0]])
   p1 = pool.apply_async(bubble_sort, [tables[1]])
   p2 = pool.apply_async(bubble_sort, [tables[2]])
   p3 = pool.apply_async(bubble_sort, [tables[3]])
   p4 = pool.apply_async(bubble_sort, [tables[4]])
   p5 = pool.apply_async(bubble_sort, [tables[5]])
   p6 = pool.apply_async(bubble_sort, [tables[6]])
   p7 = pool.apply_async(bubble_sort, [tables[7]])
   p8 = pool.apply_async(bubble_sort, [tables[8]])
   p9 = pool.apply_async(bubble_sort, [tables[9]])
   pool.close()
   pool.join()
   end = time.time()
   print('Time taken in seconds -', end - start)
