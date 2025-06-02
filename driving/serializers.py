from rest_framework import serializers
from .models import DrivingHistory
from vehicle.models import Device


class DrivingStartSerializer(serializers.Serializer):
    device_unique_id = serializers.CharField()
    user_id = serializers.IntegerField()
    start_timestamp = serializers.CharField()
    start_location = serializers.CharField()
    end_location = serializers.CharField()
    price = serializers.CharField()
    start_estimatedLoadKg = serializers.FloatField()
    
    def validate_device_unique_id(self, value):
        if not Device.objects.filter(device_unique_id=value).exists():
            raise serializers.ValidationError('Device not found')
        return value


class DrivingEndSerializer(serializers.Serializer):
    driving_log_id = serializers.IntegerField()
    device_unique_id = serializers.CharField()
    user_id = serializers.IntegerField()
    end_timestamp = serializers.CharField()
    end_estimatedLoadKg = serializers.FloatField()


class DrivingHistorySerializer(serializers.ModelSerializer):
    device_unique_id = serializers.CharField(source='device.device_unique_id', read_only=True)
    
    class Meta:
        model = DrivingHistory
        fields = '__all__'
