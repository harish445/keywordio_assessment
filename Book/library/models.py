from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=400)
    author = models.CharField(max_length=200)
    price = models.IntegerField(default=0, null=True, blank=False)
    
   