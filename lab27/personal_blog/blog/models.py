from django.db import models


# Create your models here.
class Blog(models.Model):
    main_title = models.CharField(max_length=125, unique=True, null=False)
    content = models.TextField(null=False)
    description = models.CharField(max_length=250, null=False)
    created_at = models.DateField(auto_now_add=True)
    is_public = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.main_title

    class Meta:
        db_table = 'blog'
