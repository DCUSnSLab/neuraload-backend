from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import LoggingData
from ..serializers import LoggingDataSerializer, LoggingDataListSerializer
from vehicle.models import Device
from account.models import User
from driving.models import DrivingHistory


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def load_log_view(request):
    if request.method == 'POST':
        return save_load_log(request)
    else:
        return get_load_logs(request)


def save_load_log(request):
    serializer = LoggingDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    data = serializer.validated_data
    device = Device.objects.get(device_unique_id=data['device_unique_id'])
    user = get_object_or_404(User, id=data['user_id'])
    
    # Find active driving history
    driving_history = DrivingHistory.objects.filter(
        user=user,
        device=device,
        is_completed=False
    ).first()
    
    logging_data = LoggingData.objects.create(
        user=user,
        device=device,
        driving_history=driving_history,
        timestamp=data['timestamp'],
        vehicle_speed_kmh=data['vehicleSpeedKmh'],
        gps_x=data['vehicle_position']['gps_x'],
        gps_y=data['vehicle_position']['gps_y'],
        gps_heading=data['vehicle_position']['gps_heading'],
        rpm=data['rpm'],
        brake_signal=data['brakeSignal'],
        accel_vx=data['acceleration']['Vx'],
        accel_vy=data['acceleration']['Vy'],
        laser_sensor_data=data['laserSensor'],
        estimated_load_kg=data['estimatedLoadKg']
    )
    
    return Response({
        'message': 'Logging data saved successfully',
        'logging_id': logging_data.logging_id
    }, status=status.HTTP_201_CREATED)


def get_load_logs(request):
    device_unique_id = request.query_params.get('device_unique_id')
    user_id = request.query_params.get('user_id')
    driving_history_id = request.query_params.get('driving_history_id')
    
    queryset = LoggingData.objects.all()
    
    if device_unique_id:
        queryset = queryset.filter(device__device_unique_id=device_unique_id)
    
    if user_id:
        queryset = queryset.filter(user_id=user_id)
    
    if driving_history_id:
        queryset = queryset.filter(driving_history_id=driving_history_id)
    
    queryset = queryset.order_by('-created_at')
    serializer = LoggingDataListSerializer(queryset, many=True)
    
    return Response({
        'data': serializer.data
    })
