from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'family_status',
                    'first_name', 'last_name', 'is_active', 'pfp']


admin.site.register(User, UserAdmin)
