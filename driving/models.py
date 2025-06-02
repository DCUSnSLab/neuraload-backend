from django.db import models
from django.conf import settings


class DrivingHistory(models.Model):
    driving_history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.ForeignKey('vehicle.Device', on_delete=models.CASCADE)
    
    start_timestamp = models.CharField(max_length=20)
    end_timestamp = models.CharField(max_length=20, blank=True, null=True)
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    start_estimated_load_kg = models.FloatField()
    end_estimated_load_kg = models.FloatField(blank=True, null=True)
    
    total_driving_distance = models.FloatField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'driving_history'
        
    def __str__(self):
        return f"Drive {self.driving_history_id} - {self.user.email}"
