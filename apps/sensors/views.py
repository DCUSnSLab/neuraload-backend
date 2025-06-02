from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from utils.response import success_response, error_response, created_response
from apps.devices.models import Device
from apps.users.models import User
from apps.trips.models import Trip
from .models import SensorData
from .serializers import (
    SensorDataCreateSerializer, SensorDataSerializer, SensorDataListSerializer
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_sensor_data(request):
    """센서 데이터 저장"""
    try:
        serializer = SensorDataCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            data = serializer.validated_data
            
            # 관련 객체들 조회
            device = get_object_or_404(Device, device_unique_id=data['device_unique_id'])
            user = get_object_or_404(User, id=data['user_id'])
            
            trip = None
            if data.get('driving_log_id'):
                trip = get_object_or_404(Trip, trip_id=data['driving_log_id'])
            
            # 센서 데이터 생성
            sensor_data = SensorData.objects.create(
                user=user,
                device=device,
                trip=trip,
                timestamp=data['timestamp'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                estimated_load_kg=data['estimated_load_kg'],
                speed_kmh=data['speed_kmh'],
                acceleration_x=data['acceleration_x'],
                acceleration_y=data['acceleration_y'],
                acceleration_z=data['acceleration_z'],
                gyroscope_x=data['gyroscope_x'],
                gyroscope_y=data['gyroscope_y'],
                gyroscope_z=data['gyroscope_z'],
            )
            
            return created_response(
                SensorDataSerializer(sensor_data).data,
                "Sensor data saved successfully"
            )
        
        return error_response("Sensor data save failed", serializer.errors)
        
    except Exception as e:
        return error_response(f"Sensor data save error: {str(e)}")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_sensor_data(request):
    """센서 데이터 목록 조회"""
    try:
        device_unique_id = request.query_params.get('device_unique_id')
        user_id = request.query_params.get('user_id')
        trip_id = request.query_params.get('trip_id')
        
        sensor_data = SensorData.objects.all()
        
        if device_unique_id:
            sensor_data = sensor_data.filter(device__device_unique_id=device_unique_id)
        
        if user_id:
            sensor_data = sensor_data.filter(user_id=user_id)
            
        if trip_id:
            sensor_data = sensor_data.filter(trip_id=trip_id)
        
        sensor_data = sensor_data.order_by('-created_at')
        serializer = SensorDataListSerializer(sensor_data, many=True)
        
        return success_response(
            serializer.data,
            "Sensor data retrieved successfully"
        )
        
    except Exception as e:
        return error_response(f"Sensor data list error: {str(e)}")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sensor_data_detail(request, data_id):
    """센서 데이터 상세 조회"""
    try:
        sensor_data = get_object_or_404(SensorData, data_id=data_id)
        
        return success_response(
            SensorDataSerializer(sensor_data).data,
            "Sensor data details retrieved successfully"
        )
        
    except Exception as e:
        return error_response(f"Sensor data detail error: {str(e)}")


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_sensor_data(request, data_id):
    """센서 데이터 삭제"""
    try:
        sensor_data = get_object_or_404(SensorData, data_id=data_id)
        
        # 권한 확인 - 데이터 소유자만 삭제 가능
        if sensor_data.user != request.user:
            return error_response("Access denied", status_code=403)
        
        sensor_data.delete()
        
        return success_response(
            None,
            "Sensor data deleted successfully"
        )
        
    except Exception as e:
        return error_response(f"Sensor data delete error: {str(e)}")
