from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Device, UserDeviceLink
from ..serializers import DeviceRegistrationSerializer, DeviceLinkSerializer, DeviceSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_vehicle(request):
    serializer = DeviceRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    device = serializer.save()
    
    # Auto link to current user
    UserDeviceLink.objects.create(
        user=request.user,
        device=device
    )
    
    return Response({
        'message': 'Vehicle registered successfully',
        'device': DeviceSerializer(device).data
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def link_vehicle(request):
    serializer = DeviceLinkSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    device = Device.objects.get(device_unique_id=serializer.validated_data['device_unique_id'])
    
    link, created = UserDeviceLink.objects.get_or_create(
        user=request.user,
        device=device
    )
    
    if created:
        message = 'Vehicle linked successfully'
    else:
        message = 'Vehicle already linked'
    
    return Response({
        'message': message,
        'device': DeviceSerializer(device).data
    })
