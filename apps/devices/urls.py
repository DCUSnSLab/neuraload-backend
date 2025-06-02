from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_device, name='device-create'),
    path('link/', views.link_device, name='device-link'),
    path('list/', views.list_devices, name='device-list'),
    path('<int:device_id>/', views.device_detail, name='device-detail'),
]
