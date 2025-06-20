# NeuraLoad API Testing Guide (DCUCODE Style)

## 🌐 Base URL
```
http://localhost:8000
```

## 🔑 Authentication
모든 API는 JWT 토큰 인증을 사용합니다.

---

## 👤 Users API

### 1-1. 사용자 등록
```
POST /api/users/register/
```

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
      "phone_number": "01012345678"
    },
    "tokens": {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
  }
}
```

### 1-2. 사용자 로그인
```
POST /api/users/login/
```

**Request:**
```json
{
  "email": "test@example.com",
  "password": "testpass123"
}
```

### 1-3. 사용자 프로필
```
GET /api/users/profile/
Authorization: Bearer {access_token}
```

---

## 🚛 Devices API

### 2-1. 디바이스 등록
```
POST /api/devices/
Authorization: Bearer {access_token}
```

**Request:**
```json
{
  "vehicles_model_name": "Hyundai Porter Electric",
  "max_load_capacity": 1.0,
  "device_unique_id": "#test123456789"
}
```

### 2-2. 기존 디바이스 연결
```
POST /api/devices/link/
Authorization: Bearer {access_token}
```

**Request:**
```json
{
  "device_unique_id": "#test123456789"
}
```

### 2-3. 디바이스 목록
```
GET /api/devices/list/
Authorization: Bearer {access_token}
```

### 2-4. 디바이스 상세
```
GET /api/devices/{device_id}/
Authorization: Bearer {access_token}
```

---

## 🚗 Trips API

### 3-1. 운행 시작
```
POST /api/trips/start/
Authorization: Bearer {access_token}
```

**Request:**
```json
{
  "user_id": 1,
  "device_unique_id": "#test123456789",
  "start_timestamp": "2025-06-02T10:00:00Z",
  "start_location": "서울역",
  "end_location": "부산역",
  "price": "50000",
  "start_estimatedLoadKg": 500.5
}
```

### 3-2. 운행 종료
```
POST /api/trips/end/
Authorization: Bearer {access_token}
```

**Request:**
```json
{
  "driving_log_id": 1,
  "end_timestamp": "2025-06-02T14:00:00Z",
  "end_estimatedLoadKg": 100.0
}
```

### 3-3. 운행 목록
```
GET /api/trips/?device_unique_id=#test123456789&user_id=1
Authorization: Bearer {access_token}
```

### 3-4. 운행 상세
```
GET /api/trips/{trip_id}/
Authorization: Bearer {access_token}
```

---

## 📊 Sensors API

### 4-1. 센서 데이터 저장
```
POST /api/sensors/
Authorization: Bearer {access_token}
```

**Request:**
```json
{
  "user_id": 1,
  "device_unique_id": "#test123456789",
  "driving_log_id": 1,
  "timestamp": "2025-06-02T12:00:00Z",
  "latitude": 37.5665,
  "longitude": 126.9780,
  "estimated_load_kg": 300.5,
  "speed_kmh": 60.0,
  "acceleration_x": 0.1,
  "acceleration_y": 0.05,
  "acceleration_z": 9.8,
  "gyroscope_x": 0.01,
  "gyroscope_y": 0.02,
  "gyroscope_z": 0.01
}
```

### 4-2. 센서 데이터 목록
```
GET /api/sensors/list/?device_unique_id=#test123456789&user_id=1&trip_id=1
Authorization: Bearer {access_token}
```

### 4-3. 센서 데이터 상세
```
GET /api/sensors/{data_id}/
Authorization: Bearer {access_token}
```

### 4-4. 센서 데이터 삭제
```
DELETE /api/sensors/{data_id}/delete/
Authorization: Bearer {access_token}
```

---

## 🎯 테스트 시나리오

### 완전한 워크플로우 테스트:
1. 사용자 등록 → access_token 획득
2. 디바이스 등록 → device_id 확인
3. 운행 시작 → trip_id 획득
4. 센서 데이터 저장 (여러 번)
5. 운행 종료
6. 데이터 조회 및 확인

### 오류 케이스 테스트:
- 잘못된 토큰으로 요청
- 중복 디바이스 ID 등록
- 존재하지 않는 리소스 조회
- 권한 없는 
