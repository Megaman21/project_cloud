from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.views import logout

# Create your models here.

# class Users(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(max_length=254,primary_key=True)
#     password=models.CharField(max_length=100)
from django.db.models.signals import post_save
from django.dispatch import receiver


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile picture', blank=True)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# class Customer(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
#
#     # profilePicture=models.CharField(max_length=500,default=None,blank=True,null=True)
#
#     def __str__(self):
#         return self.name


class Room(models.Model):
    room_no = models.AutoField(primary_key=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    available=models.BooleanField(default=True)

    def __str__(self):
        return str(self.room_no)


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, help_text="Enter name of the room")
    capacity = models.IntegerField()
    price = models.IntegerField(help_text="Enter price for per day stay")
    wifi_service = models.BooleanField()
    breakfast_service = models.BooleanField()
    spa_service = models.BooleanField()
    room_service = models.BooleanField()
    minibar_service = models.BooleanField()
    gym_service = models.BooleanField()
    pool_service = models.BooleanField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Images(models.Model):
    id = models.AutoField(primary_key=True)
    room_type_id = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    # url=models.URLField(help_text="URL for image stored")
    url = CloudinaryField('room picture', blank=True)

    def __str__(self):
        return str(self.id)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    room_no = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.id


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review = models.CharField(max_length=100, help_text="Enter comments")
    rating = models.PositiveIntegerField()
