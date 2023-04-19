from django import forms

from .models import product

class product_form(forms.ModelForm):
    class Meta :
        model = product
        fields = [
            'name',
            'description',
            'price'
        ]