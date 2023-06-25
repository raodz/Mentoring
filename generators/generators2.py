def get_prime_number():
    yield 2
    primes = [2]
    num = 3
    while True:
        num_is_prime = True
        for prime in primes:
            if num % prime == 0:
                num_is_prime = False
        if num_is_prime:
            primes.append(num)
            yield num
        num += 1


prime_numbers = get_prime_number()

for num in range(10):
    print(next(prime_numbers))
