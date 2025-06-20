#!/usr/bin/env python
"""
NeuraLoad 슈퍼유저 자동 생성 스크립트
"""
import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neuraload.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# 슈퍼유저 정보
superuser_data = {
    'email': 'admin@neuraload.com',
    'username': 'admin',
    'password': 'admin123456',
    'is_staff': True,
    'is_superuser': True,
    'is_active': True
}

# 기존 슈퍼유저가 있는지 확인
if User.objects.filter(email=superuser_data['email']).exists():
    print(f"슈퍼유저 '{superuser_data['email']}'가 이미 존재합니다.")
else:
    # 슈퍼유저 생성
    user = User.objects.create_user(
        email=superuser_data['email'],
        username=superuser_data['username'],
        password=superuser_data['password']
    )
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    print(f"슈퍼유저 '{superuser_data['email']}'가 생성되었습니다.")
    print(f"비밀번호: {superuser_data['password']}")
