from django.contrib import admin
from .models import Device, UserDeviceLink


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_unique_id', 'vehicles_model_name', 'max_load_capacity', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('device_unique_id', 'vehicles_model_name')


@admin.register(UserDeviceLink)
class UserDeviceLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'device', 'linked_time')
    list_filter = ('linked_time',)
    search_fields = ('user__email', 'device__device_unique_id')
