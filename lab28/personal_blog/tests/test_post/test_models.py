import pytest

from post.models import Post


@pytest.mark.django_db
def test_blog_create(blog_model_instances, user_model_instances):
    #  given
    blog1, blog2, blog3 = blog_model_instances
    user1, user2, user3 = user_model_instances
    post = Post.objects.create(
        user=user1,
        blog=blog1,
        main_title='Test main_title',
        content='Test content'
    )
    # when
    post.save()
    # then
    assert Post.objects.count() == 1


