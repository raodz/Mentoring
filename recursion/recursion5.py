def calc_gcd(a: int, b: int):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return calc_gcd(b, a % b)


def calc_lcm(a: int, b: int):
    lcm = (a * b) / calc_gcd(a, b)
    return lcm


# Tests

print(calc_lcm(15, 12))
print(calc_lcm(10, 50))
print(calc_lcm(17, 3))
