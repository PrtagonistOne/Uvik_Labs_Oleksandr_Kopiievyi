import pytest

from blog.models import Blog


@pytest.mark.django_db
def test_blog_create():
    #  given
    blog = Blog.objects.create(
        main_title='Test main_title',
        content='Test Content',
        description='Test Description',
        is_public=True
    )
    # when
    blog.save()
    # then
    assert Blog.objects.count() == 1


