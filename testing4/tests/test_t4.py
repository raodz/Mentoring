import pytest
from testing4.operations.operations_t4 import *


def test_should_raise_exception_when_list_is_empty():
    with pytest.raises(Exception):
        check_pos(0)
# check_pos() odwołuje się do zmiennej globalnej todos - jak to testować?


def test_should_raise_exception_when_pos_is_negative():
    with pytest.raises(Exception):
        check_pos(-1)


def test_should_raise_exception_when_pos_is_out_of_todos_range():
    with pytest.raises(Exception):
        check_pos(5)
