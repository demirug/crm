from django.contrib.auth.admin import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    """
    Поля для панели администрации
    Добавлен раздел Manager Info
    с полями is_manager, photo
    """
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'is_superuser', 'photo'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Manager info', {
            'fields': ('is_manager', 'photo')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Manager info', {
            'fields': ('is_manager', 'photo')
        })
    )


admin.site.register(Account, AccountAdmin)
