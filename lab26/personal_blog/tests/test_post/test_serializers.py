from collections import OrderedDict

import pytest
import io

from post.models import Post
from post.serializers import PostSerializer

from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


@pytest.mark.django_db
def test_post_serializer(blog_model_instances, user_model_instances):
    # given
    blog1, blog2, blog3 = blog_model_instances
    user1, user2, user3 = user_model_instances
    post = Post.objects.create(user=user1, blog=blog1, main_title='Testmain_title', content='SomeContent')
    # when
    post_serializer = PostSerializer(post)
    content = JSONRenderer().render(post_serializer.data)
    # then
    assert type(post_serializer.data) == ReturnDict
    assert type(content) == bytes

