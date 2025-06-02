@echo off
echo 🚀 NeuraLoad Backend Setup (DCUCODE Style)
echo ============================================

echo 📦 Starting PostgreSQL + pgAdmin...
docker-compose -f docker-compose.local.yml up -d

echo ⏳ Waiting for PostgreSQL to be ready...
timeout /t 10

echo 🐍 Setting up Conda environment...
conda info --envs | find "neuraload" >nul
if errorlevel 1 (
    echo Creating conda environment 'neuraload'...
    conda create -n neuraload python=3.11 -y
) else (
    echo Conda environment 'neuraload' already exists.
)

echo 🔄 Activating conda environment...
call conda activate neuraload

echo 🗄️ Installing PostgreSQL adapter...
conda install -c conda-forge psycopg2 -y

echo 📥 Installing Python dependencies...
pip install -r requirements.txt

echo 📄 Setting up environment variables...
if not exist ".env" (
    copy .env.local .env
    echo ✅ .env file created from .env.local
)

echo 🗑️ Removing old migration files...
for /d %%i in (apps\users apps\devices apps\trips apps\sensors) do (
    if exist "%%i\migrations" (
        pushd "%%i\migrations"
        for %%f in (*.py) do (
            if not "%%f"=="__init__.py" del "%%f"
        )
        popd
    ) else (
        mkdir "%%i\migrations"
        echo. > "%%i\migrations\__init__.py"
    )
)

echo 🔄 Creating fresh migrations...
python manage.py makemigrations users
python manage.py makemigrations devices  
python manage.py makemigrations trips
python manage.py makemigrations sensors

echo 🚀 Applying migrations...
python manage.py migrate

echo 👤 Creating superuser...
echo from apps.users.models import User; User.objects.create_superuser('admin', 'admin@neuraload.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin user already exists') | python manage.py shell

echo ✅ Setup complete!
echo.
echo 🌐 Access URLs:
echo   - Django API: http://localhost:8000
echo   - Django Admin: http://localhost:8000/admin (admin/admin123)
echo   - pgAdmin: http://localhost:5050 (admin@neuraload.com/admin123)
echo   - Health Check: http://localhost:8000/health/
echo.
echo 🚀 To start development:
echo   1. conda activate neuraload
echo   2. python manage.py runserver
echo.
echo 🛑 To stop services: docker-compose -f docker-compose.local.yml down
echo.
pause
