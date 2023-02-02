from django.db import models

from blog.models import Blog


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    main_title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.main_title

    class Meta:
        db_table = 'post'
