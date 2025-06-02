from django.urls import path
from ..views import api as views

urlpatterns = [
    path('', views.register_vehicle, name='vehicle-register'),
    path('_link/', views.link_vehicle, name='vehicle-link'),
]
