from django.urls import path
from ..views import api as views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.login_view, name='user-login'),
]
