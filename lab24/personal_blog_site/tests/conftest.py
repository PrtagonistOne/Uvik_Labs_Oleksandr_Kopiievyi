import pytest

from user.models import User


@pytest.fixture(params=['invalid', 'valid'])
def user_model_instances(request):
    invalid_username = User(username='joh*n51', password='test1', email='lennon@2.com')
    invalid_firstname = User(username='john51', password='test1', email='lennon@3.com',
                             first_name='j0hnny')
    invalid_lastname = User(username='john69', password='test1', email='lennon@4.com',
                            last_name='Br@vo')
    example_users = [invalid_username, invalid_firstname, invalid_lastname]
    expected_output = ['Username can only contain letters, digits, "_" and "-"',
                       'Your first and last name can only contain letters',
                       'Your first and last name can only contain letters']
    if request.param == 'valid':
        invalid_username.username = 'john511'
        invalid_firstname.first_name = 'Johnny'
        invalid_lastname.last_name = 'Bravo'
        example_users = [invalid_username, invalid_firstname, invalid_lastname]
        expected_output = []
    return example_users, expected_output, request.param
