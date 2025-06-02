from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from utils.response import success_response, error_response, created_response
from .models import Device, UserDeviceLink
from .serializers import (
    DeviceSerializer, DeviceCreateSerializer, 
    DeviceLinkSerializer, UserDeviceLinkSerializer
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_device(request):
    """디바이스 등록"""
    try:
        serializer = DeviceCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            device = serializer.save()
            
            # 자동으로 현재 사용자와 연결
            UserDeviceLink.objects.create(
                user=request.user,
                device=device
            )
            
            return created_response(
                DeviceSerializer(device).data,
                "Device registered successfully"
            )
        
        return error_response("Device registration failed", serializer.errors)
        
    except Exception as e:
        return error_response(f"Device registration error: {str(e)}")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def link_device(request):
    """기존 디바이스 연결"""
    try:
        serializer = DeviceLinkSerializer(data=request.data)
        
        if serializer.is_valid():
            device_unique_id = serializer.validated_data['device_unique_id']
            device = get_object_or_404(Device, device_unique_id=device_unique_id)
            
            link, created = UserDeviceLink.objects.get_or_create(
                user=request.user,
                device=device
            )
            
            message = "Device linked successfully" if created else "Device already linked"
            
            return success_response(
                DeviceSerializer(device).data,
                message
            )
        
        return error_response("Device linking failed", serializer.errors)
        
    except Exception as e:
        return error_response(f"Device linking error: {str(e)}")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_devices(request):
    """사용자의 디바이스 목록 조회"""
    try:
        user_device_links = UserDeviceLink.objects.filter(user=request.user)
        serializer = UserDeviceLinkSerializer(user_device_links, many=True)
        
        return success_response(
            serializer.data,
            "Devices retrieved successfully"
        )
        
    except Exception as e:
        return error_response(f"Device list error: {str(e)}")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def device_detail(request, device_id):
    """디바이스 상세 조회"""
    try:
        device = get_object_or_404(Device, device_id=device_id)
        
        # 사용자가 해당 디바이스에 접근 권한이 있는지 확인
        if not UserDeviceLink.objects.filter(user=request.user, device=device).exists():
            return error_response("Access denied", status_code=403)
        
        return success_response(
            DeviceSerializer(device).data,
            "Device details retrieved successfully"
        )
        
    except Exception as e:
        return error_response(f"Device detail error: {str(e)}")
