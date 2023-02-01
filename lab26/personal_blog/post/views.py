from django.contrib.auth.models import User
from django_filters.utils import translate_validation
from filters.mixins import FiltersMixin
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import UserFilter
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet, FiltersMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['content', 'main_title']
    ordering_fields = ('id', 'content', 'update_at')
    ordering = ('id',)


@api_view(['GET'])
def get_all_users(request):
    queryset = User.objects.all()
    filterset = UserFilter(request.GET, queryset=queryset)

    if not filterset.is_valid():
        raise translate_validation(filterset.errors)

    serialized_users = UserSerializer(filterset.qs, many=True)
    return Response(serialized_users.data)


class RetrieveUser(APIView):
    def get(self, request, format=None):
        user = UserSerializer(User.objects.get(pk=self.kwargs['pk']))
        return Response(user)
