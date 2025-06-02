from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_sensor_data, name='sensor-data-save'),
    path('list/', views.list_sensor_data, name='sensor-data-list'),
    path('<int:data_id>/', views.sensor_data_detail, name='sensor-data-detail'),
    path('<int:data_id>/delete/', views.delete_sensor_data, name='sensor-data-delete'),
]
