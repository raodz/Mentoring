import random

random_numbers = set(random.sample(range(5, 120), 15))
even_numbers = set()
for number in random_numbers:
    if number % 2 == 0:
        even_numbers.add(number)
print(random_numbers)
print(even_numbers)
