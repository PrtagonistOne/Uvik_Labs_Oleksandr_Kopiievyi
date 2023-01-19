from django.db import models

from .validators.custom_validators import validate_title, validate_description


class Category(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False)
    description = models.CharField(max_length=100, null=False)
    is_public = models.BooleanField(default=True, null=False)

    def clean(self):
        validate_title(self.title)
        validate_description(self.description)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = 'Categories'


# Blog should contain ManyToMany field
class Blog(models.Model):
    category = models.ManyToManyField(Category, verbose_name='Categories')
    title = models.CharField(max_length=25, unique=True, null=False)
    content = models.TextField(null=False)
    description = models.CharField(max_length=100, null=False)
    created_at = models.DateField(auto_now_add=True)
    is_public = models.BooleanField(null=False, default=True)

    def clean(self):
        validate_title(self.title)
        validate_description(self.description)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
