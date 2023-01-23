from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class UsernameBackend(BaseBackend):
    model = get_user_model()

    def authenticate(
            self, request=None, username=None, password=None):
        try:
            user = self.model.objects.get(username=username)
        except self.model.DoesNotExist:
            return None
        print(user.password, password, True)
        if self.model.check_password(self=user, raw_password=password) and user is not None:
            return user

    def get_user(self, user_id):
        try:
            return self.model.objects.get(pk=user_id)
        except self.model.DoesNotExist:
            return None
