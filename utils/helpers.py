import math
from datetime import datetime


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two GPS coordinates using Haversine formula"""
    R = 6371  # Earth's radius in kilometers
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat/2) * math.sin(dlat/2) + 
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
         math.sin(dlon/2) * math.sin(dlon/2))
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance


def parse_timestamp(timestamp_str):
    """Parse timestamp string to datetime object"""
    try:
        # Assuming format: YYMMDDHHMMSSSS
        if len(timestamp_str) == 14:
            year = 2000 + int(timestamp_str[:2])
            month = int(timestamp_str[2:4])
            day = int(timestamp_str[4:6])
            hour = int(timestamp_str[6:8])
            minute = int(timestamp_str[8:10])
            second = int(timestamp_str[10:12])
            microsecond = int(timestamp_str[12:14]) * 10000
            
            return datetime(year, month, day, hour, minute, second, microsecond)
    except:
        pass
    
    return None


def validate_device_permission(user, device):
    """Check if user has permission to access device"""
    from apps.devices.models import UserDeviceLink
    return UserDeviceLink.objects.filter(user=user, device=device).exists()
