from django.contrib import admin
from .models import LoggingData


@admin.register(LoggingData)
class LoggingDataAdmin(admin.ModelAdmin):
    list_display = ('logging_id', 'user', 'device', 'timestamp', 'estimated_load_kg', 'created_at')
    list_filter = ('created_at', 'device')
    search_fields = ('user__email', 'device__device_unique_id')
    readonly_fields = ('created_at',)
