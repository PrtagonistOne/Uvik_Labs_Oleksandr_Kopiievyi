import pytest

from functions.multiply_numbers import get_multiplied_numbers


@pytest.mark.parametrize("numbers, expected_result", [
    ((5, 10), 50),
    ((1.1, 2.62), 2.882),
    ((0, 0), 0),
    ((2.25, 10), 22.5),
    ((5.5, 10), 55.0),
    ((1, 0), 0),
])
def test_multiplied_numbers(numbers, expected_result):
    assert get_multiplied_numbers(*numbers) == expected_result
