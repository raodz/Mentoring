from math import sqrt


def check_if_prime(number: int):
    is_prime = True
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
    return is_prime


print(check_if_prime(2))
print(check_if_prime(20))
print(check_if_prime(29))
print(check_if_prime(200))
