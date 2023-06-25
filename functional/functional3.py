list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x**2, list_of_numbers))
cubes = list(map(lambda x: x**3, list_of_numbers))

print(squares)
print(cubes)
