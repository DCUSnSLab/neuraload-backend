#!/bin/sh

echo "NeuraLoad entrypoint start"

APP=/app
DATA=/data

# Create necessary directories
mkdir -p $DATA/log $DATA/static $DATA/media

# Generate secret key if it doesn't exist
if [ ! -f "$DATA/secret.key" ]; then
    echo $(cat /dev/urandom | head -1 | md5sum | head -c 32) > "$DATA/secret.key"
fi

cd $APP

# Database migration with retry
n=0
while [ $n -lt 5 ]
do
    python manage.py makemigrations &&
    python manage.py migrate --no-input &&
    python manage.py collectstatic --no-input &&
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@neuraload.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell &&
    break
    n=$(($n+1))
    echo "Failed to migrate, going to retry..."
    sleep 8
done

# Start supervisord
exec supervisord -c /app/deploy/supervisord.conf
