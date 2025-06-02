from django.db import models
from django.conf import settings


class LoggingData(models.Model):
    logging_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.ForeignKey('vehicle.Device', on_delete=models.CASCADE)
    driving_history = models.ForeignKey('driving.DrivingHistory', on_delete=models.CASCADE, null=True, blank=True)
    
    timestamp = models.CharField(max_length=20)
    vehicle_speed_kmh = models.CharField(max_length=10)
    gps_x = models.CharField(max_length=20)
    gps_y = models.CharField(max_length=20)
    gps_heading = models.IntegerField()
    rpm = models.CharField(max_length=10)
    brake_signal = models.IntegerField()
    accel_vx = models.IntegerField()
    accel_vy = models.IntegerField()
    laser_sensor_data = models.JSONField()
    estimated_load_kg = models.FloatField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'logging_data'
        
    def __str__(self):
        return f"Log {self.logging_id} - {self.device.device_unique_id}"
