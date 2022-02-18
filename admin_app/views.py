from django.shortcuts import render,redirect
from customer.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product.models import Products
from customer.forms import CustomerForm

from django.conf import settings

# Create your views here.

@login_required(login_url='/admin/login')
def admindashboard(request):
    admins = User.objects.all().order_by('username').filter(is_superuser=True)

    #it means (select * from Admins )
    return render(request, "html/dashboard.html", {'admins':admins})

@login_required(login_url='/admin/login')
def addadmins(request,*args,**kwargs):
    if request.method=='POST':
        fn=request.POST["f_name"]
        l_name=request.POST['l_name']
        uname= request.POST["uname"]
        Email= request.POST["Email"]
        pswd= request.POST["pswd"]
        user=User.objects.create_user(first_name=fn,last_name=l_name,username=uname,email=Email,password=pswd)
        user.save()
    return render(request, "html/addadmins.html", {})

@login_required(login_url='/admin/login')
def C_details(request,*args,**kwargs):
    if (request.method == 'POST'):
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        uname = request.POST['uname']
        email = request.POST['Email']
        pswd = request.POST['pswd']
        ins = User(first_name=f_name, last_name=l_name, username=uname, email=email, password=pswd)
        ins.save()
        return redirect('/admin/customers')
    else:
        customers =User.objects.all().order_by('username').filter(is_superuser=False)
        return render(request, "html/customer_details.html", {'customer': customers})


@login_required(login_url='/admin/login')
def p_details(request):
    if(request.method=='POST'):
        p_name=request.POST['p_name']
        p_category=request.POST['p_category']
        p_description=request.POST['p_description']
        p_quantity=request.POST['quantity']
        p_price=request.POST['p_price']
        if len(request.FILES) !=0:
            p_image = request.FILES['p_image']
            ins = Products(p_name=p_name, p_category=p_category, p_description=p_description,
                           p_quantity=p_quantity, p_price=p_price, p_image=p_image)
            ins.save()
            return redirect('/admin/products')

    else:
        products = Products.objects.all()
        return render(request, "html/admin_products.html", {'product': products})

#-----------------------------------login and logout views---------------------------------
def adminlogin(request):
    if request.method == 'POST':
        username=request.POST["uname"]
        pswd1 = request.POST["pswd"]

        user =authenticate(username=username,password=pswd1)
        if user is not None:
            login(request,user)
            name= user.first_name
            return redirect('/admin/dashboard')

        else:
            messages.error(request,"B=Invalid")
            return redirect("/admin/loginredirect")
    else:
        return render(request, "html/admin_login.html", {})

def login_redirect(request):
    return render(request, "html/admin_login.html")


def admin_update(request,edit_id):
    admin = User.objects.get(id=edit_id)
    print(admin)
    if (request.method == "POST"):
        form = CustomerForm(request.POST, instance=admin)
        form.username = request.POST['username']
        form.email = request.POST['email']
        form.first_name = request.POST['first_name']
        form.last_name = request.POST['last_name']
        form.password = request.POST['password']
        form.save()

    return render(request, "html/user_update.html",{'admin':admin})

def signout(request,*args,**kwargs):
    logout(request)
    return redirect('/admin/login')

