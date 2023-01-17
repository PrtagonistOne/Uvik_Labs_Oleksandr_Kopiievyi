from django.db import models


# Post Should contain Two Foreign Keys for User and Blog
class Post(models.Model):
    pass


# Comment should contain one foreign key for Post
class Comment(models.Model):
    pass
