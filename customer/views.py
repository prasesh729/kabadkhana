from django.shortcuts import render,redirect
from customer.models import User
# Create your views here.


def customer_delete(request,id):
    customer = User.objects.get(id=id)
    customer.delete()
    return redirect('/admin/customers/')