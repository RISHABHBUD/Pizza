from django.urls import path
from . import views


urlpatterns = [

    path("",views.home,name="home"),
    path("pizzalist/",views.pizzalist,name="pizzalist"),
    path("pizzalist/<int:myid>",views.pizzaview,name="pizzaview"),
    path("pizzalist/<int:myid>/checkout",views.checkout,name="checkout"),
    path("search/",views.search,name="search"),
]

