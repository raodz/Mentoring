from testing2.operations.operations_t2 import fizzbuzz


def test_should_return_fizz_when_divisible_by_3_but_not_5():
    number = 6
    assert fizzbuzz(number) == 'Fizz'


def test_should_return_buzz_when_divisible_by_5_but_not_3():
    number = 10
    assert fizzbuzz(number) == 'Buzz'


def test_should_return_fizzbuzz_when_divisible_by_3_and_5():
    number = 15
    assert fizzbuzz(number) == 'FizzBuzz'


def test_should_return_none_when_not_divisible_by_3_neither_5():
    number = 7
    assert fizzbuzz(number) is None
