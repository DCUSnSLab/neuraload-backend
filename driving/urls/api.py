from django.urls import path
from ..views import api as views

urlpatterns = [
    path('start/', views.start_driving, name='start-driving'),
    path('end/', views.end_driving, name='end-driving'),
    path('', views.get_driving_logs, name='get-driving-logs'),
]
