from pizzhut.form import PizzaShape
from pizzhut.models import Pizza
from django.shortcuts import render

# Create your views here.
def home(request):

    if request.method == "POST":
        form=PizzaShape(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=PizzaShape()
    img=Pizza.objects.all()
    return render(request,"pizzhut/home.html",{"img":img,"form":form})