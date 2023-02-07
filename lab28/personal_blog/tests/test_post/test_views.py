import pytest

from blog.models import Blog
from post.serializers import PostSerializer
from post.views import PostViewSet
from post.models import Post
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate


@pytest.mark.django_db
def test_list_post(crud_APIFactory, user_model_instances, blog_model_instances):
    # given
    post_list = PostViewSet.as_view({'get': 'list'})
    expected_results = PostSerializer(Post.objects.all(), many=True)
    # when
    request = crud_APIFactory.get('/posts/')
    force_authenticate(request, user=user_model_instances[0])
    response = post_list(request)
    # then
    assert response.status_code == 200
    assert response.data['results'] == expected_results.data


@pytest.mark.django_db
def test_retrieve_post(crud_APIFactory, user_model_instances):
    # given
    post_retrieve = PostViewSet.as_view({'get': 'retrieve'})
    post = Post.objects.get(pk=1)
    expected_results = PostSerializer(post).data
    # when
    request = crud_APIFactory.get('/posts/')
    force_authenticate(request, user=user_model_instances[0])

    response = post_retrieve(request, pk=1)
    retrieved_post_data = response.data
    # then
    assert response.status_code == 200
    assert retrieved_post_data == expected_results


@pytest.mark.django_db
def test_create_post(crud_APIFactory, user_model_instances):
    # given
    post_create = PostViewSet.as_view({'post': 'create'})
    post = Post.objects.create(
        user=User.objects.get(pk=1),
        blog=Blog.objects.get(pk=1),
        main_title='Test main_title',
        content='Test content'
    )
    post.main_title = 'This field must be unique'
    serializer = PostSerializer(post)
    # when
    request = crud_APIFactory.post('/posts/', serializer.data)
    force_authenticate(request, user=user_model_instances[0])
    response = post_create(request)
    # then
    assert response.status_code == 201
    assert response.data['main_title'] == serializer.data['main_title']


@pytest.mark.django_db
def test_put_post_403(crud_APIFactory, user_model_instances):
    # given
    post_put = PostViewSet.as_view({'put': 'update'})
    old_post = Post.objects.get(pk=1)
    old_post.main_title = 'NEW main_title'
    serializer = PostSerializer(old_post)
    # when
    request = crud_APIFactory.put('/posts/', serializer.data)
    force_authenticate(request, user=user_model_instances[0])
    response = post_put(request, pk=1)
    # then
    assert response.status_code == 403


@pytest.mark.django_db
def test_patch_post(crud_APIFactory, user_model_instances):
    # given
    post_patch = PostViewSet.as_view({'patch': 'partial_update'})
    update_new_main_title = 'NEW main_title'
    # when
    request = crud_APIFactory.patch('/posts/', {'main_title': update_new_main_title})
    force_authenticate(request, user=user_model_instances[0])
    response = post_patch(request, pk=1)
    # then
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_post_403(crud_APIFactory, user_model_instances):
    # given
    post_destroy = PostViewSet.as_view({'delete': 'destroy'})
    # when
    request = crud_APIFactory.delete('/posts/')
    force_authenticate(request, user=user_model_instances[0])
    response = post_destroy(request, pk=1)
    # then
    assert response.status_code == 403
