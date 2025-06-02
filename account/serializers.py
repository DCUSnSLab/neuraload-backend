from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('userName', 'email', 'password', 'phone_number')
        
    def to_internal_value(self, data):
        if 'userName' in data:
            data['user_name'] = data.pop('userName')
        return super().to_internal_value(data)
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['user_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_name=validated_data['user_name'],
            phone_number=validated_data.get('phone_number', '')
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password')
            if not user.is_active:
                raise serializers.ValidationError('Account is disabled')
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Email and password required')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'user_name', 'phone_number', 'created_at')
        read_only_fields = ('id', 'email', 'created_at')
