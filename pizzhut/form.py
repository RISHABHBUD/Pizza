from django import forms
from django.forms import fields
from .models import Pizza

class PizzaShape(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('shapes','sizes','toppings',)