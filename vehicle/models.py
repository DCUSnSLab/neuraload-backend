from django.db import models
from django.conf import settings


class Device(models.Model):
    device_unique_id = models.CharField(max_length=100, unique=True, primary_key=True)
    vehicles_model_name = models.CharField(max_length=100)
    max_load_capacity = models.FloatField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'devices'
        
    def __str__(self):
        return f"{self.vehicles_model_name} ({self.device_unique_id})"


class UserDeviceLink(models.Model):
    user_device_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='device_links'
    )
    device = models.ForeignKey(
        'vehicle.Device', 
        on_delete=models.CASCADE, 
        related_name='user_links'
    )
    linked_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user_device_links'
        unique_together = ('user', 'device')
        
    def __str__(self):
        return f"{self.user.email} - {self.device.device_unique_id}"
