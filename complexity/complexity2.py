def bin_search_polynomial(coeff: list, values: list):
    a, b, c, d = coeff[0], coeff[1], coeff[2], coeff[3]
    left = 0
    right = len(values) - 1
    while left <= right:
        mid = (left + right) // 2
        x = values[mid]
        polynomial_value = a * (x ** 3) + b * (x ** 2) + c * x + d
        if polynomial_value < 0:
            left = mid + 1
        elif polynomial_value > 0:
            right = mid - 1
        else:
            return x
    return 'NO'


num_of_riddles = int(input())
if num_of_riddles > 10000:
    raise ValueError('The number of riddles cannot be higher than 10 000')

pairs_of_nums = []
for i in range(num_of_riddles):
    pair = input().split()
    pair = [int(x) for x in pair]
    if pair[0] > 1012:
        raise ValueError('p cannot be higher than 1012')
    if pair[1] > 1018:
        raise ValueError('q cannot be higher than 1018')
    pairs_of_nums.append(pair)

for pair in pairs_of_nums:
    p, q = pair[0], pair[1]
    result = bin_search_polynomial([1, 0, p, -q], list(range(1018)))
    print(result)
