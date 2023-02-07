from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'DELETE']:
            return obj.user.id == request.user.id or bool(request.user and request.user.is_staff)
