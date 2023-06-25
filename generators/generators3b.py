def fibonacci():
    a = 1
    yield a
    b = 2
    while True:
        yield b
        a, b = b, a + b


fib = fibonacci()

for i in range(10):
    print(next(fib))
