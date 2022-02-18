from django import forms
from customer.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model= User
        fields="__all__"