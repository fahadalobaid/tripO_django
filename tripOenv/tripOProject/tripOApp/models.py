
import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class TripOuser(models.Model):
#     name = models.CharField(max_length=20)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name



class Profile(models.Model):
    user = models.OneToOneField( User,on_delete=models.CASCADE,)
  
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    Bio = models.TextField(max_length=180)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.user.username



class Trip(models.Model):
    owner = models.ForeignKey( Profile,on_delete=models.CASCADE,related_name="trips", )
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)

    def __str__(self):
        return self.title




