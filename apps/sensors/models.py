from django.db import models
from django.conf import settings


class SensorData(models.Model):
    """센서 데이터 모델"""
    data_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.ForeignKey('devices.Device', on_delete=models.CASCADE)
    trip = models.ForeignKey('trips.Trip', on_delete=models.CASCADE, null=True, blank=True)
    
    timestamp = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    estimated_load_kg = models.FloatField()
    speed_kmh = models.FloatField()
    
    acceleration_x = models.FloatField()
    acceleration_y = models.FloatField()
    acceleration_z = models.FloatField()
    gyroscope_x = models.FloatField()
    gyroscope_y = models.FloatField()
    gyroscope_z = models.FloatField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'sensor_data'
        
    def __str__(self):
        return f"Data {self.data_id} - {self.device.device_unique_id}"
