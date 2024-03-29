import pytest

from django.db.models import Q

from blog.models import Category


@pytest.mark.django_db
def test_category_creation():
    # given
    new_category = Category(title='Test title', description='test desc', is_public=False)
    # when
    new_category.save()
    created_category = Category.objects.get(Q(is_public=False))
    # then
    assert new_category == created_category
