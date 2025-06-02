from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """소유자만 수정 가능"""
    
    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 인증된 사용자
        if request.method in ['GET']:
            return True
        
        # 쓰기 권한은 소유자만
        return obj.user == request.user


class IsDeviceOwner(BasePermission):
    """디바이스 소유자만 접근 가능"""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        from apps.devices.models import UserDeviceLink
        
        # 사용자가 해당 디바이스에 연결되어 있는지 확인
        return UserDeviceLink.objects.filter(
            user=request.user,
            device=obj.device if hasattr(obj, 'device') else obj
        ).exists()
