#!/bin/sh

echo "NeuraLoad entrypoint start"

APP=/app
DATA=/data

# 필요한 디렉토리 생성
mkdir -p $DATA/log $DATA/config $DATA/ssl $DATA/public/upload $DATA/public/media

# 시크릿 키 생성
if [ ! -f "$DATA/config/secret.key" ]; then
    echo $(cat /dev/urandom | head -1 | md5sum | head -c 32) > "$DATA/config/secret.key"
fi

# SSL 인증서 생성 (개발용)
SSL="$DATA/ssl"
if [ ! -f "$SSL/server.key" ]; then
    openssl req -x509 -newkey rsa:2048 -keyout "$SSL/server.key" -out "$SSL/server.crt" -days 1000 \
        -subj "/C=KR/ST=Seoul/L=Seoul/O=NeuraLoad Technology Co., Ltd./OU=Backend Department/CN=`hostname`" -nodes
fi

# Nginx 설정 링크
cd $APP/deploy/nginx
ln -sf locations.conf https_locations.conf
if [ -z "$FORCE_HTTPS" ]; then
    ln -sf locations.conf http_locations.conf
else
    ln -sf https_redirect.conf http_locations.conf
fi

# IP 헤더 설정
if [ ! -z "$LOWER_IP_HEADER" ]; then
    sed -i "s/__IP_HEADER__/\$http_$LOWER_IP_HEADER/g" api_proxy.conf;
else
    sed -i "s/__IP_HEADER__/\$remote_addr/g" api_proxy.conf;
fi

# Worker 수 설정
if [ -z "$MAX_WORKER_NUM" ]; then
    export CPU_CORE_NUM=$(grep -c ^processor /proc/cpuinfo)
    if [[ $CPU_CORE_NUM -lt 2 ]]; then
        export MAX_WORKER_NUM=3
    else
        export MAX_WORKER_NUM=3
    fi
fi

cd $APP

# 데이터베이스 마이그레이션 및 초기화
n=0
while [ $n -lt 5 ]
do
    python manage.py makemigrations &&
    python manage.py migrate --no-input &&
    python manage.py shell -c "
from apps.users.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@neuraload.com', 'admin123')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
" &&
    break
    n=$(($n+1))
    echo "Failed to migrate, going to retry..."
    sleep 8
done

# 정적 파일 수집
python manage.py collectstatic --noinput

# 권한 설정
addgroup -g 12003 neuraload
adduser -u 12000 -S -G neuraload server

chown -R server:neuraload $DATA
exec supervisord -c /app/deploy/supervisord.conf
