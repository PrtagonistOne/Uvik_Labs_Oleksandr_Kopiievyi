import pytest
from blog.serializers import BlogSerializer

from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.renderers import JSONRenderer


@pytest.mark.django_db
def test_post_serializer(blog_model_instances):
    # given
    post_serializer = BlogSerializer(blog_model_instances, many=True)
    # when
    content = JSONRenderer().render(post_serializer.data)
    # then
    assert type(post_serializer.data) == ReturnList
    assert type(content) == bytes
