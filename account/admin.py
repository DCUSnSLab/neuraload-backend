from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'user_name', 'phone_number', 'is_active', 'created_at')
    list_filter = ('is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'username', 'user_name', 'phone_number')
    ordering = ('-created_at',)
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {
            'fields': ('user_name', 'phone_number', 'bank_name', 'account_number')
        }),
        ('날짜 정보', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
        ('추가 정보', {
            'fields': ('user_name', 'phone_number', 'bank_name', 'account_number')
        }),
    )
