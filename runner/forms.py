from django import forms
from .models import ErrandRequest

class ErrandRequestForm(forms.ModelForm):
    class Meta:
        model = ErrandRequest
        fields = ['service', 'description']