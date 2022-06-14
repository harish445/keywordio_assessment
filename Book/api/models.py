from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=200, unique=True)
    #REQUIRED_FIELDS = ['username']
    #USERNAME_FIELD = 'email'
    
    def get_username(self):
        return self.email    