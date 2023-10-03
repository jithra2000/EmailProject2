from django.db import models

# Create your models here.
class DataEntry(models.Model):
    UserName=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)
    Email=models.EmailField()