from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from .models import Post

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    main_title = serializers.CharField(validators=[
        UniqueValidator(queryset=Post.objects.all())
    ])

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['first_name', 'last_name']
            )
        ]
