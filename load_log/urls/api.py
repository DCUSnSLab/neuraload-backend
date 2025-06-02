from django.urls import path
from ..views import api as views

urlpatterns = [
    path('', views.load_log_view, name='load-log'),
]
