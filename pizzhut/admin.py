from django.contrib import admin

# Register your models here.
from .models import Pizza , Order
admin.site.register(Pizza)
admin.site.register(Order)