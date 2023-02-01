import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from blog.models import Blog
from post.models import Post


@pytest.fixture()
def blog_model_instances():
    blog1 = Blog.objects.create(
        main_title='Test main_title1',
        content='Test Content1',
        description='Test Description1',
        is_public=True
    )
    blog2 = Blog.objects.create(
        main_title='Test main_title2',
        content='Test Content2',
        description='Test Description2',
        is_public=True
    )
    blog3 = Blog.objects.create(
        main_title='fg main_title3',
        content='SDF Content3',
        description='sdf Description3',
        is_public=False
    )
    return blog1, blog2, blog3


@pytest.fixture()
def user_model_instances():
    user1 = User.objects.create(username='prota', password=1)
    user2 = User.objects.create(username='prota1', password=2)
    user3 = User.objects.create(username='prota2', password=3)

    return user1, user2, user3


@pytest.fixture()
def post_model_instances(blog_model_instances, user_model_instances):
    blog1, blog2, blog3 = blog_model_instances
    user1, user2, user3 = user_model_instances
    post1 = Post.objects.create(
        user=user1,
        blog=blog1,
        main_title='Test main_title',
        content='Test content'
    )
    post2 = Post.objects.create(
        user=user2,
        blog=blog2,
        main_title='Test2 main_title',
        content='Test2 content'
    )
    post3 = Post.objects.create(
        user=user3,
        blog=blog3,
        main_title='Test3 main_title',
        content='Test3 content'
    )
    return post1, post2, post3


@pytest.fixture()
def crud_APIFactory(post_model_instances):
    post1, post2, post3 = post_model_instances
    dummy_instances_data = (post1, post2, post3)
    for instance in dummy_instances_data:
        instance.save()
    return APIRequestFactory()
