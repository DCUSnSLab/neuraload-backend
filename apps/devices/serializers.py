from rest_framework import serializers
from .models import Device, UserDeviceLink


class DeviceSerializer(serializers.ModelSerializer):
    """디바이스 시리얼라이저"""
    
    class Meta:
        model = Device
        fields = ['device_id', 'vehicle_model', 'max_load_capacity', 'device_unique_id', 'created_at']
        read_only_fields = ['device_id', 'created_at']


class DeviceCreateSerializer(serializers.ModelSerializer):
    """디바이스 생성 시리얼라이저"""
    vehicles_model_name = serializers.CharField(source='vehicle_model')
    
    class Meta:
        model = Device
        fields = ['vehicles_model_name', 'max_load_capacity', 'device_unique_id']


class DeviceLinkSerializer(serializers.Serializer):
    """디바이스 연결 시리얼라이저"""
    device_unique_id = serializers.CharField()
    
    def validate_device_unique_id(self, value):
        try:
            Device.objects.get(device_unique_id=value)
            return value
        except Device.DoesNotExist:
            raise serializers.ValidationError("Device not found")


class UserDeviceLinkSerializer(serializers.ModelSerializer):
    """사용자-디바이스 연결 시리얼라이저"""
    device = DeviceSerializer(read_only=True)
    
    class Meta:
        model = UserDeviceLink
        fields = ['device', 'linked_at']
