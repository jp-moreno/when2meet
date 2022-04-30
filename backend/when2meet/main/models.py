from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pic = models.ImageField(upload_to="profile_pics", default="default_profile_pic.jpg")
    class Meta:
        ordering = ["-date_joined"]

class TimeRange(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

class Event(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    time = models.ManyToManyField(TimeRange) 

class Available(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time = models.ManyToManyField(TimeRange) 