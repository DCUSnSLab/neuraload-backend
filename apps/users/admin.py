from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# 인라인 클래스들 (다른 앱에서 import)
class UserDeviceLinkInline(admin.TabularInline):
    from apps.devices.models import UserDeviceLink
    model = UserDeviceLink
    extra = 0
    readonly_fields = ('linked_at',)
    autocomplete_fields = ('device',)

class TripInline(admin.TabularInline):
    from apps.trips.models import Trip
    model = Trip
    extra = 0
    fields = ('trip_id', 'device', 'start_time', 'is_completed')
    readonly_fields = ('trip_id',)
    autocomplete_fields = ('device',)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """사용자 어드민"""
    list_display = ('email', 'username', 'phone_number', 'is_active', 'is_staff', 'created_at')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('-created_at',)
    
    # 필드셋 정의
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {
            'fields': ('phone_number', 'created_at', 'updated_at')
        }),
    )
    
    # 읽기 전용 필드
    readonly_fields = ('created_at', 'updated_at')
    
    # 추가 시 필드셋
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('추가 정보', {
            'fields': ('email', 'phone_number')
        }),
    )
    
    # 인라인 (사용자 페이지에서 연결된 디바이스와 트립 보기)
    inlines = [UserDeviceLinkInline, TripInline]
