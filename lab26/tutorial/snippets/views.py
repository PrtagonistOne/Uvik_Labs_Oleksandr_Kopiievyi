from rest_framework import renderers, viewsets, generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions

from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Snippet.objects.filter(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
