from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API Routes
    path('api/users/', include('apps.users.urls')),
    path('api/devices/', include('apps.devices.urls')),
    path('api/trips/', include('apps.trips.urls')),
    path('api/sensors/', include('apps.sensors.urls')),
    
    # Health Check
    path('health/', lambda request: HttpResponse('OK')),
]

# Media files serving for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Import HttpResponse for health check
from django.http import HttpResponse
