#!/bin/sh
set -e

echo "🚀 NeuraLoad Backend Starting..."

# PostgreSQL 연결 대기
echo "⏳ Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "✅ PostgreSQL started"

# 데이터베이스 마이그레이션
echo "🔄 Running database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# 정적 파일 수집
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# 기본 슈퍼유저 생성
echo "👤 Creating default superuser..."
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neuraload.settings')
django.setup()

from apps.users.models import User
if not User.objects.filter(email='admin@neuraload.com').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@neuraload.com', 
        password='admin123456'
    )
    print('Default superuser created: admin@neuraload.com / admin123456')
else:
    print('Default superuser already exists')
"

echo "✅ NeuraLoad Backend Ready!"

# Gunicorn으로 서버 시작
exec gunicorn neuraload.wsgi:application --bind 0.0.0.0:8000 --workers 3
