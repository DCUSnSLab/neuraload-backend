from django.db import models
from django.conf import settings


class Device(models.Model):
    """디바이스 모델"""
    device_id = models.AutoField(primary_key=True)
    vehicle_model = models.CharField(max_length=100)
    max_load_capacity = models.FloatField()
    device_unique_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'devices'
        
    def __str__(self):
        return f"{self.vehicle_model} - {self.device_unique_id}"


class UserDeviceLink(models.Model):
    """사용자-디바이스 연결 모델"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    linked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user_device_links'
        unique_together = ['user', 'device']
        
    def __str__(self):
        return f"{self.user.email} - {self.device.device_unique_id}"
