# NeuraLoad Backend

NeuraLoad is a logistics management platform backend for real-time vehicle weight estimation and delivery tracking.

## Features

- User authentication and management
- Vehicle registration and linking
- Real-time driving log management  
- Sensor data collection and weight estimation
- REST API for mobile/web clients

## Tech Stack

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL 15
- **Web Server**: Nginx + Gunicorn
- **Deployment**: Docker + Supervisord

## Project Structure

```
neuraload-backend/
├── account/                 # User authentication & management
├── vehicle/                 # Vehicle/device management
├── driving/                 # Driving history & trip management
├── logging/                 # Real-time sensor data logging
├── utils/                   # Common utilities
├── neuraload/               # Django configuration
├── deploy/                  # Deployment files
│   ├── nginx/              # Nginx configuration
│   ├── requirements.txt
│   ├── supervisord.conf
│   └── entrypoint.sh
├── data/                    # Data storage (auto-created)
│   ├── log/                # Application logs
│   ├── media/              # Media files
│   └── static/             # Static files
├── Dockerfile
├── docker-compose.yml       # Development
├── docker-compose.prod.yml  # Production
└── manage.py
```

## API Endpoints

### Account Management
- `POST /api/account/register/` - User registration
- `POST /api/account/login/` - User login

### Vehicle Management  
- `POST /api/vehicles/` - Register vehicle
- `POST /api/vehicles_link/` - Link existing vehicle

### Driving Management
- `POST /api/driving_log/start/` - Start driving session
- `POST /api/driving_log/end/` - End driving session
- `GET /api/driving_log/` - Get driving logs

### Load Data
- `POST /api/load_log/` - Save sensor data with weight estimation
- `GET /api/load_log/` - Get load log data

## Quick Start

### Development

```bash
# Clone repository
git clone <repository-url>
cd neuraload-backend

# Start with Docker
docker-compose up --build -d

# Check services
docker-compose logs -f
```

**Access:**
- API Server: http://localhost:8000
- Admin Panel: http://localhost:8000/admin (`admin` / `admin123`)

### Production

```bash
# Set environment variables
cp .env.prod .env
# Edit .env with production values

# Deploy
docker-compose -f docker-compose.prod.yml up --build -d
```

## Docker Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Run Django commands
docker-compose exec web python manage.py shell
docker-compose exec web python manage.py migrate

# Access database
docker-compose exec db psql -U postgres -d neuraload
```

## Environment Variables

### Development
```bash
# Uses default values in docker-compose.yml
DEBUG=True
DATABASE_URL=postgresql://postgres:password@db:5432/neuraload
```

### Production (.env.prod)
```bash
SECRET_KEY=your-production-secret-key
DB_PASSWORD=your-secure-db-password  
ALLOWED_HOSTS=your-domain.com
```

## Architecture

```
Client → Nginx (Port 80) → Gunicorn (Django) → PostgreSQL
```

## Database Schema

- **User**: User authentication and profile
- **Device**: Vehicle/device information  
- **UserDeviceLink**: Many-to-many relationship
- **DrivingHistory**: Trip/driving session records
- **LoggingData**: Real-time sensor data with weight estimation

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test with `docker-compose up`
5. Submit pull request

## License

Proprietary software for NeuraLoad platform.
