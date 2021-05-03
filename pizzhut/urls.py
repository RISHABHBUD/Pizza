from django.urls import path
from . import views


urlpatterns = [

    path("home/",views.home,name="home"),
    path("home/pizzalist",views.pizzalist,name="pizzalist"),
    path("home/pizzalist/<int:myid>",views.pizzaview,name="pizzaview"),
]

