from django import forms
from product.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model= Products
        fields="__all__"