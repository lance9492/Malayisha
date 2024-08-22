from django import forms
from .models import Delivery

class DeliveryRequestForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['delivery_country', 'delivery_city', 'delivery_address']