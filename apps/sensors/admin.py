from django.contrib import admin
from .models import SensorData


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    """센서 데이터 어드민"""
    list_display = (
        'data_id', 'user', 'device', 'trip', 'timestamp',
        'latitude', 'longitude', 'estimated_load_kg', 'speed_kmh', 'created_at'
    )
    list_filter = ('created_at', 'timestamp', 'device')
    search_fields = (
        'user__email', 'device__device_unique_id', 
        'trip__trip_id'
    )
    ordering = ('-created_at',)
    
    # 읽기 전용 필드
    readonly_fields = ('data_id', 'created_at')
    
    # 자동완성 필드
    autocomplete_fields = ('user', 'device', 'trip')
    
    # 날짜 계층
    date_hierarchy = 'created_at'
    
    # 한 페이지당 표시할 항목 수
    list_per_page = 50
    
    # 필드셋
    fieldsets = (
        ('기본 정보', {
            'fields': ('user', 'device', 'trip', 'timestamp')
        }),
        ('위치 정보', {
            'fields': ('latitude', 'longitude', 'speed_kmh')
        }),
        ('화물 정보', {
            'fields': ('estimated_load_kg',)
        }),
        ('가속도 센서', {
            'fields': ('acceleration_x', 'acceleration_y', 'acceleration_z'),
            'classes': ('collapse',)
        }),
        ('자이로스코프 센서', {
            'fields': ('gyroscope_x', 'gyroscope_y', 'gyroscope_z'),
            'classes': ('collapse',)
        }),
        ('시스템 정보', {
            'fields': ('data_id', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    # 액션
    actions = ['export_as_csv']
    
    def export_as_csv(self, request, queryset):
        """선택된 센서 데이터를 CSV로 내보내기"""
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sensor_data.csv"'
        
        writer = csv.writer(response)
        writer.writerow([
            'data_id', 'user_email', 'device_id', 'trip_id', 'timestamp',
            'latitude', 'longitude', 'estimated_load_kg', 'speed_kmh',
            'acceleration_x', 'acceleration_y', 'acceleration_z',
            'gyroscope_x', 'gyroscope_y', 'gyroscope_z'
        ])
        
        for obj in queryset:
            writer.writerow([
                obj.data_id, obj.user.email, obj.device.device_unique_id,
                obj.trip.trip_id if obj.trip else '', obj.timestamp,
                obj.latitude, obj.longitude, obj.estimated_load_kg, obj.speed_kmh,
                obj.acceleration_x, obj.acceleration_y, obj.acceleration_z,
                obj.gyroscope_x, obj.gyroscope_y, obj.gyroscope_z
            ])
        
        return response
    export_as_csv.short_description = '선택된 센서 데이터를 CSV로 내보내기'
