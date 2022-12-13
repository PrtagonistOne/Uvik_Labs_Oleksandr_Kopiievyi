import pytest

import functions
from functions.balanced_parantheses import check_balanced_parentheses


@pytest.fixture(params=['balanced', 'unbalanced'])
def generate_brackets_input(request, mocker):
    example_input = ['{[]{()}}', '[(){}]', '([{}])']
    expected_output = [True, True, True]
    if request.param == 'unbalanced':
        example_input = ['[{}{}(]', '{][{()}}', '[][[][']
        expected_output = [False, False, False]
        mocker.patch.object(functions.balanced_parantheses,
                            'get_executing_module_name',
                            return_value='This is mocked data')

    return example_input, expected_output, request.param


def test_balanced_parentheses(generate_brackets_input):
    test_input, expected_output, parameter = generate_brackets_input
    output = [check_balanced_parentheses(bracket) for bracket in test_input]
    assert output == expected_output
