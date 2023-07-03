from testing1.operations.operations_t1 import check_if_prime


class TestIsPrime:

    def test_should_return_false_for_minus_one(self):
        number = -1
        assert not check_if_prime(number)

    def test_should_return_false_for_zero(self):
        number = 0
        assert not check_if_prime(number)

    def test_should_return_false_for_one(self):
        number = 1
        assert not check_if_prime(number)

    def test_should_return_true_for_two(self):
        number = 2
        assert check_if_prime(number)

    def test_should_return_true_for_three(self):
        number = 3
        assert check_if_prime(number)

    def test_should_return_false_for_four(self):
        number = 4
        assert not check_if_prime(number)
