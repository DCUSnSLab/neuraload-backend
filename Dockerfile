FROM python:3.11-alpine3.18

ENV NEURALOAD_ENV production

ADD . /app
WORKDIR /app

# 시스템 의존성 설치
RUN apk add --update --no-cache \
    gcc \
    linux-headers \
    musl-dev \
    postgresql-dev \
    build-base \
    nginx \
    openssl \
    curl \
    supervisor \
    jpeg-dev \
    zlib-dev \
    freetype-dev

# Python 의존성 설치
RUN pip install --no-cache-dir -r /app/requirements.txt

# 빌드 의존성 제거 (이미지 크기 최적화)
RUN apk del build-base --purge

# 헬스체크
HEALTHCHECK --interval=5s --retries=3 CMD python /app/deploy/health_check.py

# 엔트리포인트 설정  
ENTRYPOINT ["/bin/sh", "/app/docker-entrypoint.sh"]
