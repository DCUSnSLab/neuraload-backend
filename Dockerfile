FROM python:3.11-alpine

ENV NEURALOAD_ENV production

ADD . /app
WORKDIR /app

# Install system dependencies
RUN apk add --update --no-cache \
    build-base \
    nginx \
    supervisor \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    gcc \
    musl-dev \
    linux-headers

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/deploy/requirements.txt

# Clean up build dependencies
RUN apk del build-base --purge

ENTRYPOINT ["/bin/sh", "/app/deploy/entrypoint.sh"]
