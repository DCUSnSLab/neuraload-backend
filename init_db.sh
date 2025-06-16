#!/bin/bash
set -x

if [[ ! -f manage.py ]]; then
   echo "No manage.py, wrong location"
   exit 1
fi

sleep 2
docker rm -f neuraload-postgres-dev neuraload-pgadmin-dev
docker run -it -d -e POSTGRES_DB=neuraload_db -e POSTGRES_USER=neuraload_user -e POSTGRES_PASSWORD=neuraload_password -p 5432:5432 --name neuraload-postgres-dev postgres:15-alpine
docker run -it -d -e PGADMIN_DEFAULT_EMAIL=admin@neuraload.com -e PGADMIN_DEFAULT_PASSWORD=admin123 -p 5050:80 --name neuraload-pgadmin-dev dpage/pgadmin4:latest

if [ "$1" = "--migrate" ]; then
   sleep 5
   
   # 환경변수 설정
   export DB_HOST=localhost
   export DB_PORT=5432
   export DB_NAME=neuraload_db
   export DB_USER=neuraload_user
   export DB_PASSWORD=neuraload_password
   
   # 데이터베이스 사용자 생성 (PostgreSQL 컨테이너 내에서)
   docker exec neuraload-postgres-dev psql -U postgres -c "CREATE DATABASE neuraload_db;"
   docker exec neuraload-postgres-dev psql -U postgres -c "CREATE USER neuraload_user WITH PASSWORD 'neuraload_password';"
   docker exec neuraload-postgres-dev psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE neuraload_db TO neuraload_user;"
   docker exec neuraload-postgres-dev psql -U postgres -c "ALTER USER neuraload_user CREATEDB;"
   
   # Django 마이그레이션
   python manage.py makemigrations
   python manage.py migrate
   
   # 슈퍼유저 생성
   echo "from apps.users.models import User; User.objects.create_superuser('admin', 'admin@neuraload.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin already exists')" | python manage.py shell
   
   echo "Database setup complete!"
   echo "Backend: python manage.py runserver"
   echo "pgAdmin: http://localhost:5050"
fi