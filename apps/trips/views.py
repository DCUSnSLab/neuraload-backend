from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from utils.response import success_response, error_response, created_response
from apps.devices.models import Device
from apps.users.models import User
from .models import Trip
from .serializers import TripStartSerializer, TripEndSerializer, TripSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_trip(request):
    """운행 시작"""
    try:
        serializer = TripStartSerializer(data=request.data)
        
        if serializer.is_valid():
            data = serializer.validated_data
            device = get_object_or_404(Device, device_unique_id=data['device_unique_id'])
            user = get_object_or_404(User, id=data['user_id'])
            
            trip = Trip.objects.create(
                user=user,
                device=device,
                start_time=data['start_time'],
                start_location=data['start_location'],
                end_location=data['end_location'],
                price=data['price'],
                start_load_kg=data['start_load_kg']
            )
            
            return created_response({
                'driving_log_id': trip.trip_id,
                'data': TripSerializer(trip).data
            }, "Trip started successfully")
        
        return error_response("Trip start failed", serializer.errors)
        
    except Exception as e:
        return error_response(f"Trip start error: {str(e)}")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def end_trip(request):
    """운행 종료"""
    try:
        serializer = TripEndSerializer(data=request.data)
        
        if serializer.is_valid():
            data = serializer.validated_data
            trip = get_object_or_404(Trip, trip_id=data['trip_id'])
            
            trip.end_time = data['end_time']
            trip.end_load_kg = data['end_load_kg']
            trip.is_completed = True
            trip.save()
            
            return success_response(
                TripSerializer(trip).data,
                "Trip ended successfully"
            )
        
        return error_response("Trip end failed", serializer.errors)
        
    except Exception as e:
        return error_response(f"Trip end error: {str(e)}")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_trips(request):
    """운행 기록 목록 조회"""
    try:
        device_unique_id = request.query_params.get('device_unique_id')
        user_id = request.query_params.get('user_id')
        
        trips = Trip.objects.all()
        
        if device_unique_id:
            trips = trips.filter(device__device_unique_id=device_unique_id)
        
        if user_id:
            trips = trips.filter(user_id=user_id)
        
        trips = trips.order_by('-created_at')
        serializer = TripSerializer(trips, many=True)
        
        return success_response(
            serializer.data,
            "Trips retrieved successfully"
        )
        
    except Exception as e:
        return error_response(f"Trip list error: {str(e)}")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def trip_detail(request, trip_id):
    """운행 기록 상세 조회"""
    try:
        trip = get_object_or_404(Trip, trip_id=trip_id)
        
        return success_response(
            TripSerializer(trip).data,
            "Trip details retrieved successfully"
        )
        
    except Exception as e:
        return error_response(f"Trip detail error: {str(e)}")
