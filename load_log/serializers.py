from rest_framework import serializers
from .models import LoggingData
from vehicle.models import Device


class LoggingDataSerializer(serializers.Serializer):
    timestamp = serializers.CharField()
    device_unique_id = serializers.CharField()
    user_id = serializers.IntegerField()
    vehicleSpeedKmh = serializers.CharField()
    vehicle_position = serializers.DictField()
    rpm = serializers.CharField()
    brakeSignal = serializers.IntegerField()
    acceleration = serializers.DictField()
    laserSensor = serializers.ListField()
    estimatedLoadKg = serializers.FloatField()
    
    def validate_device_unique_id(self, value):
        if not Device.objects.filter(device_unique_id=value).exists():
            raise serializers.ValidationError('Device not found')
        return value
    
    def validate_vehicle_position(self, value):
        required_fields = ['gps_x', 'gps_y', 'gps_heading']
        for field in required_fields:
            if field not in value:
                raise serializers.ValidationError(f'{field} is required in vehicle_position')
        return value
    
    def validate_acceleration(self, value):
        required_fields = ['Vx', 'Vy']
        for field in required_fields:
            if field not in value:
                raise serializers.ValidationError(f'{field} is required in acceleration')
        return value


class LoggingDataListSerializer(serializers.ModelSerializer):
    device_unique_id = serializers.CharField(source='device.device_unique_id', read_only=True)
    vehicle_position = serializers.SerializerMethodField()
    acceleration = serializers.SerializerMethodField()
    
    class Meta:
        model = LoggingData
        fields = '__all__'
    
    def get_vehicle_position(self, obj):
        return {
            'gps_x': obj.gps_x,
            'gps_y': obj.gps_y,
            'gps_heading': obj.gps_heading
        }
    
    def get_acceleration(self, obj):
        return {
            'Vx': obj.accel_vx,
            'Vy': obj.accel_vy
        }
