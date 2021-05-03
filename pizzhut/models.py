from django.db import models



# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=50,default="pizzaname")
    shape1 = models.CharField(max_length=50,default="",blank=True)
    shape2 = models.CharField(max_length=50,default="",blank=True)


    size1 = models.CharField(max_length=50,default="")
    size2 = models.CharField(max_length=50,default="",blank=True)
    size3= models.CharField(max_length=50,default="",blank=True)
    size4 = models.CharField(max_length=50,default="",blank=True)
    size5 = models.CharField(max_length=50,default="",blank=True)
    size6 = models.CharField(max_length=50,default="",blank=True)

    toppings1 = models.CharField(max_length=15)
    toppings2 = models.CharField(max_length=15)
    toppings3 = models.CharField(max_length=15,blank=True)
    toppings4 = models.CharField(max_length=15,blank=True)
    toppings5 = models.CharField(max_length=15,blank=True)
    toppings6 = models.CharField(max_length=15,blank=True)
    toppings7 = models.CharField(max_length=15,blank=True)
    toppings8 = models.CharField(max_length=15,blank=True)
    toppings9 = models.CharField(max_length=15,blank=True)
    toppings10 = models.CharField(max_length=15,blank=True)
    toppings11 = models.CharField(max_length=15,blank=True)
    toppings12 = models.CharField(max_length=15,blank=True)
    toppings13 = models.CharField(max_length=15,blank=True)
    toppings14 = models.CharField(max_length=15,blank=True)
    toppings15 = models.CharField(max_length=15,blank=True)
    toppings16 = models.CharField(max_length=15,blank=True)
    toppings17 = models.CharField(max_length=15,blank=True)
    toppings18 = models.CharField(max_length=15,blank=True)
    toppings19 = models.CharField(max_length=15,blank=True)
    toppings20 = models.CharField(max_length=15,blank=True)

class Order(models.Model):
    size = models.CharField(max_length=30,default="mediumm")
    shape = models.CharField(max_length=50,default="circle")
    toppings = models.CharField(max_length=20,default="onion")

