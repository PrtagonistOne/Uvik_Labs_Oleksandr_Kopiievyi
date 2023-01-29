from django.db import models

from user.models import User
from blog.models import Blog

from blog.validators.custom_validators import validate_title
from post.validation.custom_validation import validate_comment_content


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def clean(self):
        validate_title(self.title)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(null=False, default=False)

    def clean(self):
        validate_comment_content(self.content)

    def get_post_username(self):
        return self.post.user

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'
