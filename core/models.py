from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AppUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length = 100)
    username = models.CharField(max_length=200, unique="True", blank=False)
    password = models.CharField(max_length=200, blank=False)
    is_Admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(auto_now_add=True)
    ##
      
    
   
