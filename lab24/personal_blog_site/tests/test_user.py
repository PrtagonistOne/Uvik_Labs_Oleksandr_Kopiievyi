import pytest

from django.core.exceptions import ValidationError
from user.models import User


@pytest.mark.django_db
def test_username_create_user(user_model_instances):
    users, expected_results, param = user_model_instances
    results = []
    if param == 'invalid':
        for user in users:
            with pytest.raises(ValidationError) as user_error:
                user.clean()
            error_text = user_error.value.message
            results.append(error_text)
        assert User.objects.count() == 0
    else:
        for user in users:
            user.clean()
            user.save()
        assert User.objects.count() == 3
    assert results == expected_results
