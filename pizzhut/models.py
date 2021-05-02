from django.db import DefaultConnectionProxy, models
from multiselectfield import MultiSelectField

# Create your models here.
class Pizza(models.Model):
    shape = (
        ('regular',"Regular"),
        ('square',"Square"),
    )
    shapes = models.CharField(max_length=10,choices=shape,default="Invalid")
    size = (
        ('small',"Small"),
        ('medium',"Medium"),
        ('large',"Large"),
    )

    sizes = models.CharField(max_length=10,choices=size,default="Invalid")
    topping = (
        ('onion',"onion"),
        ('capsicum',"capsicum"),
        ('tomato',"tomato"),
        ('corn',"corn"),
    )
    toppings = MultiSelectField(choices=topping,default="Invalid")



