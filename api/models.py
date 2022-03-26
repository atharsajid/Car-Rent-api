import numbers
from django.db import models

# Create your models here.


class Users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.IntegerField()
    address = models.CharField(max_length=250,)
    emailaddress = models.CharField(max_length=70,)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str___(self):
        return self.title


class CarList(models.Model):
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    car = models.IntegerField()
    rent = models.CharField(max_length=250,)
    rating = models.CharField(max_length=70,)
    imagepath = models.CharField(max_length=250,)

    def __str___(self):
        return self.title
