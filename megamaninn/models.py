from django.db import models

# Create your models here.

# class Users(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(max_length=254,primary_key=True)
#     password=models.CharField(max_length=100)
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    profilePicture=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Room(models.Model):
    id=models.AutoField(primary_key=True)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.id