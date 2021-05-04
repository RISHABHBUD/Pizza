from django.db import models



# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=50,default="pizzaname")
    shape1 = models.CharField(max_length=50,default="",blank=True)
    shape2 = models.CharField(max_length=50,default="",blank=True)


    size1 = models.CharField(max_length=50,default="")
    size2 = models.CharField(max_length=50,default="",blank=True)
    size3= models.CharField(max_length=50,default="",blank=True)


    toppings1 = models.CharField(max_length=15)
    toppings2 = models.CharField(max_length=15,blank=True)
    toppings3 = models.CharField(max_length=15,blank=True)
    toppings4 = models.CharField(max_length=15,blank=True)
    toppings5 = models.CharField(max_length=15,blank=True)
    toppings6 = models.CharField(max_length=15,blank=True)

class Order(models.Model):
    size = models.CharField(max_length=30,default="mediumm")
    shape = models.CharField(max_length=50,default="circle")
    toppings = models.CharField(max_length=20,default="onion")

