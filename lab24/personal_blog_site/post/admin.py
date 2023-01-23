from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog', 'title', 'content',
                    'created_at', 'updated_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_post_username', 'content', 'created_at', 'updated_at',
                    'is_deleted']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
