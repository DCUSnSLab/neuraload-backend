from django.contrib import admin
from .models import DrivingHistory


@admin.register(DrivingHistory)
class DrivingHistoryAdmin(admin.ModelAdmin):
    list_display = ('driving_history_id', 'user', 'device', 'start_location', 'end_location', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('user__email', 'device__device_unique_id', 'start_location', 'end_location')
