from math import sqrt

def check_if_prime(checked_number: int):
    if checked_number < 2:
        return False
    for number in range(2, int(sqrt(checked_number) + 1)):
        if checked_number % number == 0:
            return False
    return True
