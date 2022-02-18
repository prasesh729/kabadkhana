from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from customer.models import User
from django.contrib.auth import authenticate,login,logout
from product.models import *
from product.forms import *
from customer.forms import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views import View

# Create your views here.
def productpage_view(request,*args,**kwargs):
    product = Products.objects.all()
    paginator = Paginator(product, 16)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
    }
    return render(request, "html/product.html", data)

def loginpage(request):
    if request.method == 'POST':
        username=request.POST["uname"]
        pswd1 = request.POST["pswd"]
        user =authenticate(username=username,password=pswd1)
        if user is not None:
            login(request,user)
            return render(request, "html/landing_page.html", {})
        else:
            return redirect("/login")

    else:
        return render(request, "html/Loginfrom.html", {})


def customer_register(request):
    if (request.method == 'POST'):
        uname = request.POST['uname']
        email = request.POST['Email']
        pswd = request.POST['pswd']
        f_name = request.POST['fi_name']
        l_name = request.POST['la_name']
        ins = User.objects.create_user( username=uname, email=email, password=pswd,first_name=f_name,last_name=l_name)
        ins.save()
        return redirect('http://127.0.0.1:8001/')
    else:
        return render(request, "html/mem_register.html", {})

def mainpage(request,*args,**kwargs):
    return render(request,"html/landing_page.html",{})

class Product_p(View):
    def post(self,request,id):
        product=request.POST.get("product")
        cart = request.session.get('cart')
        if cart:
            quantity =cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] =1
        else:
            cart={}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('/')

    def get(self,request,id):

        single_product = get_object_or_404(Products, pk=id)


        single_product = get_object_or_404(Products, pk=id)


        data = {
            'single_product': single_product,
        }
        return render(request, "html/product_details.html", data)





@login_required(login_url='/login')
def shoppingpage(request,*args,**kwargs):
    return render(request, "html/shopping_cart.html", {})


def aboutpage(request,*args,**kwargs):
    return render(request, "html/about_us.html", {})

def Adminloginpage(request,*args,**kwargs):
    return render(request, "html/admin_login.html", {})

@login_required(login_url='/login')
def profilet(request,profile_id):
    customer = User.objects.get(id=profile_id)
    print(request.POST)
    if(request.method=="POST"):
        form = CustomerForm(request.POST, instance=customer)
        form.username = request.POST['username']
        form.email = request.POST['email']
        form.first_name = request.POST['first_name']
        form.last_name = request.POST['last_name']
        form.password = request.POST['password']
        print(form)
        form.save()





    return render(request, "html/profile.html", {'customers':customer})

def logout_customer(request):
    logout(request)
    return redirect('http://127.0.0.1:8001/')



@login_required(login_url='/login')
def user_add_product(request,*args,**kwargs):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
    return render(request, "html/add_user_product.html", {})

@login_required(login_url='/login')
def user_product(request,user_id):
    products = Products.objects.filter(user_id_id=user_id)
    return render(request, "html/user_product.html", {'product':products})


@login_required(login_url='/login')

def user_product_delete(request,product_id):
    product =Products.objects.get(product_id=product_id)
    product.delete()
    return redirect('/')


def purchasepage(request):
    return render(request, "html/purchase.html")

@login_required(login_url='/login')
def product_edit(request,p_edit_id):
    products = Products.objects.get(product_id=p_edit_id)
    if (request.method == "POST"):
        form = ProductForm(request.POST, instance=products)
        form.p_name = request.POST['p_name']
        form.p_category = request.POST['p_category']
        form.p_description = request.POST['p_description']
        form.p_quantity = request.POST['p_quantity']
        form.p_price = request.POST['p_price']
        form.img = request.FILES['p_image']
        print(form)
        form.save()
    return render(request, "html/edit_product.html",{'pr':products})


def purchasepage(request,):
    return render(request, "html/purchase.html", {})

