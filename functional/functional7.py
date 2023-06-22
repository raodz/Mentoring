nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_nums = list(map(lambda x: x**2 if x % 2 == 0 else x, nums))
print(new_nums)
