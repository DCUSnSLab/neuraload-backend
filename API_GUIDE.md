# API Documentation

## Authentication
JWT 토큰 인증 사용
```http
Authorization: Bearer {access_token}
```

---

## Users API

### 1. 사용자 등록
**Endpoint:** `POST /api/users/register/`
**Authentication:** None

**Request:**
```json
{
  "userName": "testuser",
  "email": "test@example.com",
  "password": "testpass123",
  "phone_number": "01012345678"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "user": {
      "id": 1,
      "username": "testuser",
      "email": "test@example.com",
      "phone_number": "01012345678",
      "created_at": "2025-08-11T15:13:36.327638+09:00"
    },
    "tokens": {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
  }
}
```

### 2. 사용자 로그인
**Endpoint:** `POST /api/users/login/`
**Authentication:** None

**Request:**
```json
{
  "email": "test@example.com",
  "password": "testpass123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "user": {
      "id": 1,
      "username": "testuser",
      "email": "test@example.com",
      "phone_number": "01012345678",
      "created_at": "2025-08-11T15:13:36.327638+09:00"
    },
    "tokens": {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
  }
}
```

### 3. 사용자 프로필 조회
**Endpoint:** `GET /api/users/profile/`
**Authentication:** Required

**Response:**
```json
{
  "success": true,
  "message": "Profile retrieved successfully",
  "data": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "phone_number": "01012345678",
    "created_at": "2025-08-11T15:13:36.327638+09:00"
  }
}
```

---

## Devices API

### 1. 디바이스 등록
**Endpoint:** `POST /api/devices/`
**Authentication:** Required

**Request:**
```json
{
  "vehicles_model_name": "Hyundai Porter Electric",
  "max_load_capacity": 1.5,
  "device_unique_id": "#test123456789"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Device registered successfully",
  "data": {
    "device_id": 1,
    "vehicle_model": "Hyundai Porter Electric",
    "max_load_capacity": 1.5,
    "device_unique_id": "#test123456789",
    "created_at": "2025-08-11T15:14:06.371771+09:00"
  }
}
```

### 2. 기존 디바이스 연결
**Endpoint:** `POST /api/devices/link/`
**Authentication:** Required

**Request:**
```json
{
  "device_unique_id": "#test123456789"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Device linked successfully",
  "data": {
    "device_id": 1,
    "vehicle_model": "Hyundai Porter Electric",
    "max_load_capacity": 1.5,
    "device_unique_id": "#test123456789",
    "created_at": "2025-08-11T15:14:06.371771+09:00"
  }
}
```

### 3. 디바이스 목록 조회
**Endpoint:** `GET /api/devices/list/`
**Authentication:** Required

**Response:**
```json
{
  "success": true,
  "message": "Devices retrieved successfully",
  "data": [
    {
      "device": {
        "device_id": 1,
        "vehicle_model": "Hyundai Porter Electric",
        "max_load_capacity": 1.5,
        "device_unique_id": "#test123456789",
        "created_at": "2025-08-11T15:14:06.371771+09:00"
      },
      "linked_at": "2025-08-11T15:14:06.373672+09:00"
    }
  ]
}
```

### 4. 디바이스 상세 조회
**Endpoint:** `GET /api/devices/{device_id}/`
**Authentication:** Required

**Response:**
```json
{
  "success": true,
  "message": "Device details retrieved successfully",
  "data": {
    "device_id": 1,
    "vehicle_model": "Hyundai Porter Electric",
    "max_load_capacity": 1.5,
    "device_unique_id": "#test123456789",
    "created_at": "2025-08-11T15:14:06.371771+09:00"
  }
}
```

---

## 🚗 Trips API

### 1. 운행 시작
**Endpoint:** `POST /api/trips/start/`
**Authentication:** Required

**Request:**
```json
{
  "user_id": 1,
  "device_unique_id": "#test123456789",
  "start_timestamp": "2025-08-11T15:15:00Z",
  "start_location": "서울역",
  "end_location": "부산역",
  "price": "50000",
  "start_estimatedLoadKg": 500.5
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trip started successfully",
  "data": {
    "driving_log_id": 1,
    "data": {
      "driving_history_id": 1,
      "start_timestamp": "2025-08-11T15:15:00Z",
      "end_timestamp": null,
      "start_location": "서울역",
      "end_location": "부산역",
      "price": "50000",
      "start_estimated_load_kg": 500.5,
      "end_estimated_load_kg": null,
      "total_driving_distance": null,
      "is_completed": false,
      "created_at": "2025-08-11T15:14:30.469668+09:00"
    }
  }
}
```

### 2. 운행 종료
**Endpoint:** `POST /api/trips/end/`
**Authentication:** Required

**Request:**
```json
{
  "driving_log_id": 1,
  "end_timestamp": "2025-08-11T18:00:00Z",
  "end_estimatedLoadKg": 100.0
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trip ended successfully",
  "data": {
    "driving_history_id": 1,
    "start_timestamp": "2025-08-11T15:15:00Z",
    "end_timestamp": "2025-08-11T18:00:00Z",
    "start_location": "서울역",
    "end_location": "부산역",
    "price": "50000",
    "start_estimated_load_kg": 500.5,
    "end_estimated_load_kg": 100.0,
    "total_driving_distance": null,
    "is_completed": true,
    "created_at": "2025-08-11T15:14:30.469668+09:00"
  }
}
```

### 3. 운행 목록 조회
**Endpoint:** `GET /api/trips/`
**Authentication:** Required

**Query Parameters:**
- `device_unique_id` (optional): 디바이스 고유 ID
- `user_id` (optional): 사용자 ID

**Example:** `GET /api/trips/?device_unique_id=#test123456789&user_id=1`

**Response:**
```json
{
  "success": true,
  "message": "Trips retrieved successfully",
  "data": [
    {
      "driving_history_id": 1,
      "start_timestamp": "2025-08-11T15:15:00Z",
      "end_timestamp": "2025-08-11T18:00:00Z",
      "start_location": "서울역",
      "end_location": "부산역",
      "price": "50000",
      "start_estimated_load_kg": 500.5,
      "end_estimated_load_kg": 100.0,
      "total_driving_distance": null,
      "is_completed": true,
      "created_at": "2025-08-11T15:14:30.469668+09:00"
    }
  ]
}
```

### 4. 운행 상세 조회
**Endpoint:** `GET /api/trips/{trip_id}/`
**Authentication:** Required

**Response:**
```json
{
  "success": true,
  "message": "Trip details retrieved successfully",
  "data": {
    "driving_history_id": 1,
    "start_timestamp": "2025-08-11T15:15:00Z",
    "end_timestamp": "2025-08-11T18:00:00Z",
    "start_location": "서울역",
    "end_location": "부산역",
    "price": "50000",
    "start_estimated_load_kg": 500.5,
    "end_estimated_load_kg": 100.0,
    "total_driving_distance": null,
    "is_completed": true,
    "created_at": "2025-08-11T15:14:30.469668+09:00"
  }
}
```

---

## 📊 Sensors API

### 1. 센서 데이터 저장
**Endpoint:** `POST /api/sensors/`
**Authentication:** Required

**Request:**
```json
{
  "user_id": 1,
  "device_unique_id": "#test123456789",
  "driving_log_id": 1,
  "timestamp": "2025-08-11T15:16:00Z",
  "latitude": 37.5665,
  "longitude": 126.9780,
  "estimated_load_kg": 450.3,
  "speed_kmh": 60.0,
  "acceleration_x": 0.1,
  "acceleration_y": 0.05,
  "acceleration_z": 9.8,
  "gyroscope_x": 0.01,
  "gyroscope_y": 0.02,
  "gyroscope_z": 0.01
}
```

**Response:**
```json
{
  "success": true,
  "message": "Sensor data saved successfully",
  "data": {
    "logging_id": 1,
    "timestamp": "2025-08-11T15:16:00Z",
    "latitude": 37.5665,
    "longitude": 126.978,
    "estimated_load_kg": 450.3,
    "speed_kmh": 60.0,
    "acceleration_x": 0.1,
    "acceleration_y": 0.05,
    "acceleration_z": 9.8,
    "gyroscope_x": 0.01,
    "gyroscope_y": 0.02,
    "gyroscope_z": 0.01,
    "created_at": "2025-08-11T15:14:51.310879+09:00"
  }
}
```

### 2. 센서 데이터 목록 조회
**Endpoint:** `GET /api/sensors/list/`
**Authentication:** Required

**Query Parameters:**
- `device_unique_id` (optional): 디바이스 고유 ID
- `user_id` (optional): 사용자 ID
- `trip_id` (optional): 운행 ID

**Example:** `GET /api/sensors/list/?device_unique_id=#test123456789&user_id=1&trip_id=1`

**Response:**
```json
{
  "success": true,
  "message": "Sensor data retrieved successfully",
  "data": [
    {
      "data_id": 1,
      "device_unique_id": "#test123456789",
      "user_email": "test@example.com",
      "timestamp": "2025-08-11T15:16:00Z",
      "latitude": 37.5665,
      "longitude": 126.978,
      "estimated_load_kg": 450.3,
      "speed_kmh": 60.0,
      "created_at": "2025-08-11T15:14:51.310879+09:00"
    }
  ]
}
```

### 3. 센서 데이터 상세 조회
**Endpoint:** `GET /api/sensors/{data_id}/`
**Authentication:** Required

**Response:**
```json
{
  "success": true,
  "message": "Sensor data details retrieved successfully",
  "data": {
    "logging_id": 1,
    "timestamp": "2025-08-11T15:16:00Z",
    "latitude": 37.5665,
    "longitude": 126.978,
    "estimated_load_kg": 450.3,
    "speed_kmh": 60.0,
    "acceleration_x": 0.1,
    "acceleration_y": 0.05,
    "acceleration_z": 9.8,
    "gyroscope_x": 0.01,
    "gyroscope_y": 0.02,
    "gyroscope_z": 0.01,
    "created_at": "2025-08-11T15:14:51.310879+09:00"
  }
}
```

### 4. 센서 데이터 삭제
**Endpoint:** `DELETE /api/sensors/{data_id}/delete/`
**Authentication:** Required

**Response:**
```json
{
  "success": true,
  "message": "Sensor data deleted successfully",
  "data": null
}
```

---
---

## 응답 형식

### 성공
```json
{
  "success": true,
  "message": "Success message",
  "data": { ... }
}
```

### 오류
```json
{
  "success": false,
  "message": "Error message",
  "errors": { ... }
}
```