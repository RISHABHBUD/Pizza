from .models import Order, Pizza
from django.shortcuts import render

def home(request):
    return render(request,"pizzhut/home.html")


def pizzalist(request):
    piz = Pizza.objects.all()
    return render(request,'pizzhut/pizzalist.html',{'piz':piz})

def pizzaview(request,myid):
    if request.method=="POST":
        size = request.POST.get('pizza_size','')
        shape = request.POST.get('pizza_shape','')
        toppings = request.POST.get('toppings','')

        ord = Order(size=size,shape=shape,toppings=toppings)
        ord.save()
    pizview = Pizza.objects.filter(id=myid)

    return render(request,'pizzhut/pizzaview.html',{'pizview':pizview})