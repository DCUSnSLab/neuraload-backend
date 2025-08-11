# NeuraLoad Backend
## Docker 실행

```bash
git clone <repository-url>
cd neuraload-backend

docker compose up --build -d

docker compose ps
```
## 로컬 개발 환경

### 1. 환경 설정

```bash
# Python 가상환경 생성
conda create -n neuraload python=3.11
conda activate neuraload

# 의존성 설치
pip install -r requirements.txt
```

### 2. 데이터베이스 설정

```bash
# PostgreSQL 시작 (Docker)
docker compose up postgres -d

# 환경변수 설정 (.env 파일 생성)
DEBUG=True
DB_HOST=localhost
DB_PORT=5432
DB_NAME=neuraload_db
DB_USER=neuraload_user
DB_PASSWORD=neuraload_password
```

### 3. Django 설정

```bash
# 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 슈퍼유저 생성
python manage.py createsuperuser

# 개발 서버 실행
python manage.py runserver 8000
```