from django.db import models
from django.conf import settings


class Trip(models.Model):
    """운행 기록 모델"""
    trip_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.ForeignKey('devices.Device', on_delete=models.CASCADE)
    
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    start_load_kg = models.FloatField()
    end_load_kg = models.FloatField(blank=True, null=True)
    
    total_distance = models.FloatField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'trips'
        
    def __str__(self):
        return f"Trip {self.trip_id} - {self.user.email}"
