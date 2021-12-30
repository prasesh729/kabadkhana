"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from landingpage.views import productpage_view
from landingpage.views import loginpage

from landingpage.views import mainpage
from landingpage.views import aboutpage
from landingpage.views import shoppingpage
from landingpage.views import customer_register
from landingpage.views import profilet
from landingpage.views import logout_customer
from landingpage.views import Product_p
from landingpage import views

from landingpage.views import Adminloginpage

urlpatterns = [
    path('product/', productpage_view),
    path('AAdmin/', admin.site.urls),
    path('login/',loginpage),
    path('product/<int:id>/', Product_p.as_view(), name='product_detail'),
    path('register/',customer_register,name="register"),
    path('', mainpage),
    path('aboutus/',aboutpage),
    path('admin/',include("admin_app.urls")),
    path('shopping_cart/',shoppingpage),
    path('profile/<int:profile_id>',profilet),
    path('c_logout/',logout_customer),
    path('add_product/',views.user_add_product),
    path('user_delete/<int:product_id>',views.user_product_delete),
    path('user_product/<int:user_id>',views.user_product),
    path('purchase/',views.purchasepage),

]
