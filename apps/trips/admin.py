from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    """운행 기록 어드민"""
    list_display = (
        'trip_id', 'user', 'device', 'start_time', 'end_time', 
        'start_load_kg', 'end_load_kg', 'is_completed', 'created_at'
    )
    list_filter = ('is_completed', 'created_at', 'start_time')
    search_fields = (
        'user__email', 'device__device_unique_id', 
        'start_location', 'end_location'
    )
    ordering = ('-created_at',)
    
    # 읽기 전용 필드
    readonly_fields = ('trip_id', 'created_at')
    
    # 자동완성 필드
    autocomplete_fields = ('user', 'device')
    
    # 필터 옵션
    date_hierarchy = 'created_at'
    
    # 필드셋
    fieldsets = (
        ('기본 정보', {
            'fields': ('user', 'device', 'is_completed')
        }),
        ('운행 정보', {
            'fields': (
                'start_time', 'end_time', 'start_location', 'end_location',
                'total_distance', 'price'
            )
        }),
        ('화물 정보', {
            'fields': ('start_load_kg', 'end_load_kg')
        }),
        ('시스템 정보', {
            'fields': ('trip_id', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    # 액션
    actions = ['mark_as_completed', 'mark_as_incomplete']
    
    def mark_as_completed(self, request, queryset):
        """선택된 운행을 완료로 표시"""
        updated = queryset.update(is_completed=True)
        self.message_user(request, f'{updated}개의 운행을 완료로 표시했습니다.')
    mark_as_completed.short_description = '선택된 운행을 완료로 표시'
    
    def mark_as_incomplete(self, request, queryset):
        """선택된 운행을 미완료로 표시"""
        updated = queryset.update(is_completed=False)
        self.message_user(request, f'{updated}개의 운행을 미완료로 표시했습니다.')
    mark_as_incomplete.short_description = '선택된 운행을 미완료로 표시'
