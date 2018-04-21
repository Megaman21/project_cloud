from django.db import models

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254,primary_key=True)
    password=models.CharField(max_length=100)