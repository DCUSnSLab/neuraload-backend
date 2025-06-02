from rest_framework import serializers
from .models import SensorData
from apps.devices.models import Device
from apps.trips.models import Trip


class SensorDataCreateSerializer(serializers.Serializer):
    """센서 데이터 생성 시리얼라이저"""
    user_id = serializers.IntegerField()
    device_unique_id = serializers.CharField()
    driving_log_id = serializers.IntegerField(required=False)
    timestamp = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    estimated_load_kg = serializers.FloatField()
    speed_kmh = serializers.FloatField()
    acceleration_x = serializers.FloatField()
    acceleration_y = serializers.FloatField()
    acceleration_z = serializers.FloatField()
    gyroscope_x = serializers.FloatField()
    gyroscope_y = serializers.FloatField()
    gyroscope_z = serializers.FloatField()


class SensorDataSerializer(serializers.ModelSerializer):
    """센서 데이터 시리얼라이저"""
    logging_id = serializers.IntegerField(source='data_id', read_only=True)
    
    class Meta:
        model = SensorData
        fields = [
            'logging_id', 'timestamp', 'latitude', 'longitude',
            'estimated_load_kg', 'speed_kmh', 'acceleration_x',
            'acceleration_y', 'acceleration_z', 'gyroscope_x',
            'gyroscope_y', 'gyroscope_z', 'created_at'
        ]


class SensorDataListSerializer(serializers.ModelSerializer):
    """센서 데이터 목록 시리얼라이저"""
    device_unique_id = serializers.CharField(source='device.device_unique_id', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = SensorData
        fields = [
            'data_id', 'device_unique_id', 'user_email',
            'timestamp', 'latitude', 'longitude', 'estimated_load_kg',
            'speed_kmh', 'created_at'
        ]
