from freezegun import freeze_time
from testing5.operations.operations_t5 import calc_diff


@freeze_time('2021-11-03T09:22:38+00:00')
def test_should_return_time_difference():
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None
    }
    assert calc_diff(case) == 10
