from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """사용자 등록 시리얼라이저"""
    password = serializers.CharField(write_only=True, min_length=8)
    userName = serializers.CharField(source='username')
    
    class Meta:
        model = User
        fields = ['userName', 'email', 'password', 'phone_number']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number')
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    """사용자 로그인 시리얼라이저"""
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                    return data
                else:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Invalid email or password.")
        else:
            raise serializers.ValidationError("Must include email and password.")


class UserSerializer(serializers.ModelSerializer):
    """사용자 정보 시리얼라이저"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at']
        read_only_fields = ['id', 'created_at']
