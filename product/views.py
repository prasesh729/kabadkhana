from django.shortcuts import render,redirect
from product.models import Products
# Create your views here.

def product_edit(request,product_id):
    if(request.method=='POST'):
        product=Products.objects.get(product_id=product_id)

    return render(request,'html/admin_products.html')


def product_delete(request,product_id):
    product =Products.objects.get(product_id=product_id)
    product.delete()
    return redirect('/admin/products')

