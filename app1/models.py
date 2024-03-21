from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(User):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phno = models.IntegerField()

class CoachInfos(models.Model):
    Image = models.ImageField()
    Name = models.CharField(max_length=100)
    Sports = models.CharField(max_length=50)
    Summary = models.TextField()
    Charge = models.IntegerField()
    username = models.TextField()
    password =  models.TextField()

class BookedCoach(models.Model):
    Coach = models.TextField()
    Sports = models.TextField()
    Bookdate = models.TextField()
    Time = models.TextField(blank=True)
    Bookeddate = models.TextField()
    Bookedby = models.TextField()

class UserDetail(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phno = models.IntegerField()
    Username = models.TextField()
    Password = models.TextField()

    # def __str__(self):
    #     return self.Username

class Slot(models.Model):
    Slotname = models.CharField(max_length=50)
    Timerange = models.TextField()

class BookedSlot(models.Model):
    Bookingid = models.TextField()
    Slotname = models.CharField(max_length=50)
    Timerange = models.TextField()
    Bookedby = models.TextField()
    Bookeddate = models.TextField()
    Slotdate = models.TextField()
