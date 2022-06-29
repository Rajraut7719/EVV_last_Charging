from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    full_name=models.CharField(max_length=50,error_messages={'required':'Enter Full Name'})
    mobile=models.CharField(max_length=14,help_text='Enter mobile no')
    email=models.EmailField(max_length=50)