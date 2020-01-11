
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from administration.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_voting_chief', 'is_voting_node',)
    list_filter = ('is_staff', 'is_voting_chief', 'is_voting_node')


    fieldsets = (
        ('Data',{
            'fields':('username','first_name','last_name','password','email')
        }),
        ('Management',{
            'fields':('is_active','is_staff','is_voting_chief','is_voting_node',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        """Cannot delete. Only set as unactive"""
        return False


admin.site.register(User, CustomUserAdmin)
