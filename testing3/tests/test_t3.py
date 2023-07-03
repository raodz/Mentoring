import pytest
from testing3.operations.operations_t3 import partition, quick_sort


def test_should_return_3_for_current_array():
    arr = [2, 9, 5, 2, 0, 1, 4, 3]
    assert partition(arr, 0, len(arr) - 1) == 3


def test_should_return_1_for_one_element_array():
    arr = [2]
    assert partition(arr, 0, len(arr) - 1) == 1


def test_should_raise_index_error_for_empty_array():
    arr = []
    with pytest.raises(IndexError):
        partition(arr, 0, len(arr) - 1)


def test_should_return_sorted_array():
    original_array = [5, 2, 7, 1, -2, 4, 7, 4, 9, 0]
    expected_result = [-2, 0, 1, 2, 4, 4, 5, 7, 7, 9]
    actual_result = original_array.copy()
    quick_sort(actual_result)
    assert expected_result == actual_result
