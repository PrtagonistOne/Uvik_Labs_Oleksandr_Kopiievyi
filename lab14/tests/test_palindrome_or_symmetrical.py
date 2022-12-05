import pytest

from functions.palindrome_or_symmetrical import evaluate_palindrome_or_symmetrical


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert evaluate_palindrome_or_symmetrical(maybe_palindrome)['Palindrome'] == expected_result


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", False),
    ("Bob", False),
    ("Never odd or even", False),
    ("Do geese see God?", False),
    ("khokho", True),
    ("amaama", True),
])
def test_is_symmetrical(maybe_palindrome, expected_result):
    assert evaluate_palindrome_or_symmetrical(maybe_palindrome)['Symmetrical'] == expected_result
