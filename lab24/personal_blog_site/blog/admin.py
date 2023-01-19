from django.contrib import admin
from .models import Category, Blog


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_public']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'description', 'created_at',
                    'is_public']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
