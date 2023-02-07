from django.contrib.auth.models import User
from django_filters.utils import translate_validation
from filters.mixins import FiltersMixin
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import UserFilter
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, UserSerializer, RegisterSerializer


class PostViewSet(viewsets.ModelViewSet, FiltersMixin):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['content', 'main_title']
    ordering_fields = ('id', 'content', 'updated_at')
    ordering = ('id',)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser(), IsOwnerOrReadOnly()]
        return [permissions.IsAuthenticated()]


@api_view(['GET'])
def get_all_users(request):
    queryset = User.objects.all()
    filterset = UserFilter(request.GET, queryset=queryset)

    if not filterset.is_valid():
        raise translate_validation(filterset.errors)

    serialized_users = UserSerializer(filterset.qs, many=True)
    return Response(serialized_users.data)


class RetrieveUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        user = UserSerializer(User.objects.get(pk=self.kwargs['pk']))
        return Response(user.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
