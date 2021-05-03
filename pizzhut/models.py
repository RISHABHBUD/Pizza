from django.db import DefaultConnectionProxy, models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from multiselectfield import MultiSelectField

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=50,default="pizzaname")
    shape1 = models.CharField(max_length=50,default=" ",blank=True)
    shape2 = models.CharField(max_length=50,default=" ",blank=True)
    size1 = models.CharField(max_length=50,default=" ",blank=True)
    size2 = models.CharField(max_length=50,default=" ",blank=True)
    size3= models.CharField(max_length=50,default=" ",blank=True)
    size4 = models.CharField(max_length=50,default=" ",blank=True)
    size5 = models.CharField(max_length=50,default=" ",blank=True)
    size6 = models.CharField(max_length=50,default=" ",blank=True)

class Order(models.Model):
    size = models.CharField(max_length=30,default="mediumm")
    shape = models.CharField(max_length=50,default="circle")

