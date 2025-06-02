from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import DrivingHistory
from ..serializers import DrivingStartSerializer, DrivingEndSerializer, DrivingHistorySerializer
from vehicle.models import Device
from account.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_driving(request):
    serializer = DrivingStartSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    data = serializer.validated_data
    device = Device.objects.get(device_unique_id=data['device_unique_id'])
    user = get_object_or_404(User, id=data['user_id'])
    
    driving_history = DrivingHistory.objects.create(
        user=user,
        device=device,
        start_timestamp=data['start_timestamp'],
        start_location=data['start_location'],
        end_location=data['end_location'],
        price=data['price'],
        start_estimated_load_kg=data['start_estimatedLoadKg']
    )
    
    return Response({
        'message': 'Driving started successfully',
        'driving_log_id': driving_history.driving_history_id,
        'data': DrivingHistorySerializer(driving_history).data
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def end_driving(request):
    serializer = DrivingEndSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    data = serializer.validated_data
    driving_history = get_object_or_404(DrivingHistory, driving_history_id=data['driving_log_id'])
    
    driving_history.end_timestamp = data['end_timestamp']
    driving_history.end_estimated_load_kg = data['end_estimatedLoadKg']
    driving_history.is_completed = True
    driving_history.save()
    
    return Response({
        'message': 'Driving ended successfully',
        'data': DrivingHistorySerializer(driving_history).data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_driving_logs(request):
    device_unique_id = request.query_params.get('device_unique_id')
    user_id = request.query_params.get('user_id')
    
    queryset = DrivingHistory.objects.all()
    
    if device_unique_id:
        queryset = queryset.filter(device__device_unique_id=device_unique_id)
    
    if user_id:
        queryset = queryset.filter(user_id=user_id)
    
    queryset = queryset.order_by('-created_at')
    serializer = DrivingHistorySerializer(queryset, many=True)
    
    return Response({
        'data': serializer.data
    })
