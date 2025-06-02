from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.email
