from rest_framework import serializers
from .models import Device, UserDeviceLink


class DeviceRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('vehicles_model_name', 'max_load_capacity', 'device_unique_id')


class DeviceLinkSerializer(serializers.Serializer):
    device_unique_id = serializers.CharField()
    
    def validate_device_unique_id(self, value):
        if not Device.objects.filter(device_unique_id=value).exists():
            raise serializers.ValidationError('Device not found')
        return value


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_unique_id', 'vehicles_model_name', 'max_load_capacity', 'created_at')
