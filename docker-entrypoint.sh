#!/bin/bash
set -e

echo "🚀 NeuraLoad Backend Starting..."

# PostgreSQL 연결 대기
echo "⏳ Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "✅ PostgreSQL started"

# 데이터베이스 마이그레이션
echo "🔄 Running database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# 정적 파일 수집
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# 슈퍼유저 생성 (환경변수가 있는 경우)
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "👤 Creating superuser..."
    python manage.py shell -c "
from apps.users.models import User
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"
fi

echo "✅ NeuraLoad Backend Ready!"

# 전달된 명령어 실행
exec "$@"
