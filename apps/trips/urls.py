from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_trip, name='trip-start'),
    path('end/', views.end_trip, name='trip-end'),
    path('', views.list_trips, name='trip-list'),
    path('<int:trip_id>/', views.trip_detail, name='trip-detail'),
]
