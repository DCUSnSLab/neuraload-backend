from django.contrib import admin
from .models import Device, UserDeviceLink


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """디바이스 어드민"""
    list_display = ('device_id', 'vehicle_model', 'max_load_capacity', 'device_unique_id', 'created_at')
    list_filter = ('vehicle_model', 'created_at')
    search_fields = ('device_unique_id', 'vehicle_model')
    ordering = ('-created_at',)
    
    # 읽기 전용 필드
    readonly_fields = ('device_id', 'created_at')
    
    # 필드셋
    fieldsets = (
        ('기본 정보', {
            'fields': ('device_unique_id', 'vehicle_model', 'max_load_capacity')
        }),
        ('시스템 정보', {
            'fields': ('device_id', 'created_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserDeviceLink)
class UserDeviceLinkAdmin(admin.ModelAdmin):
    """사용자-디바이스 연결 어드민"""
    list_display = ('user', 'device', 'linked_at')
    list_filter = ('linked_at',)
    search_fields = ('user__email', 'device__device_unique_id')
    ordering = ('-linked_at',)
    
    # 읽기 전용 필드
    readonly_fields = ('linked_at',)
    
    # 자동완성 필드
    autocomplete_fields = ('user', 'device')


# 인라인 어드민 (User 페이지에서 연결된 디바이스 보기)
class UserDeviceLinkInline(admin.TabularInline):
    model = UserDeviceLink
    extra = 0
    readonly_fields = ('linked_at',)
