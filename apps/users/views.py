from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from utils.response import success_response, error_response, created_response
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """사용자 등록"""
    try:
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)
            
            return created_response({
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, "User registered successfully")
        
        return error_response("Registration failed", serializer.errors)
        
    except Exception as e:
        return error_response(f"Registration error: {str(e)}")


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """사용자 로그인"""
    try:
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)
            
            return success_response({
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, "Login successful")
        
        return error_response("Login failed", serializer.errors)
        
    except Exception as e:
        return error_response(f"Login error: {str(e)}")


@api_view(['GET'])
def profile(request):
    """사용자 프로필 조회"""
    try:
        return success_response(
            UserSerializer(request.user).data,
            "Profile retrieved successfully"
        )
    except Exception as e:
        return error_response(f"Profile error: {str(e)}")
