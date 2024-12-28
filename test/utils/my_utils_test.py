from src.utils import my_utils

def test_random_float_with_step():
    start = 0.3
    end = 0.4
    step = 0.01

    for i in range(10**6):
        actual = my_utils.random_float_with_step(start, end, step)

        assert actual >= 0.3
        assert actual <= 0.4
        _assert_has_two_decimal_places(actual)

def _assert_has_two_decimal_places(number):
    parts = str(number).split('.')
    assert len(parts) == 2
    assert len(parts[1]) <= 2