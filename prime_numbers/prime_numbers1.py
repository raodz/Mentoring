def get_primes(number_of_primes: int):
    primes = [2]
    current_number = 3
    while True:
        if len(primes) == number_of_primes:
            return primes
        is_current_number_prime = True
        for prime in primes:
            if current_number % prime == 0:
                is_current_number_prime = False
        if is_current_number_prime:
            primes.append(current_number)
        current_number += 1


print(get_primes(20))
