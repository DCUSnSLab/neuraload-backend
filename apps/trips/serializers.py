from rest_framework import serializers
from .models import Trip
from apps.devices.models import Device


class TripStartSerializer(serializers.Serializer):
    """운행 시작 시리얼라이저"""
    user_id = serializers.IntegerField()
    device_unique_id = serializers.CharField()
    start_timestamp = serializers.CharField(source='start_time')
    start_location = serializers.CharField()
    end_location = serializers.CharField()
    price = serializers.CharField()
    start_estimatedLoadKg = serializers.FloatField(source='start_load_kg')


class TripEndSerializer(serializers.Serializer):
    """운행 종료 시리얼라이저"""
    driving_log_id = serializers.IntegerField(source='trip_id')
    end_timestamp = serializers.CharField(source='end_time')
    end_estimatedLoadKg = serializers.FloatField(source='end_load_kg')


class TripSerializer(serializers.ModelSerializer):
    """운행 기록 시리얼라이저"""
    driving_history_id = serializers.IntegerField(source='trip_id', read_only=True)
    start_timestamp = serializers.CharField(source='start_time', read_only=True)
    end_timestamp = serializers.CharField(source='end_time', read_only=True)
    start_estimated_load_kg = serializers.FloatField(source='start_load_kg', read_only=True)
    end_estimated_load_kg = serializers.FloatField(source='end_load_kg', read_only=True)
    total_driving_distance = serializers.FloatField(source='total_distance', read_only=True)
    
    class Meta:
        model = Trip
        fields = [
            'driving_history_id', 'start_timestamp', 'end_timestamp',
            'start_location', 'end_location', 'price',
            'start_estimated_load_kg', 'end_estimated_load_kg',
            'total_driving_distance', 'is_completed', 'created_at'
        ]
