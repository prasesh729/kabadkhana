from django.contrib import admin
from django.urls import path,include
from admin_app import views


urlpatterns = [
    path('dashboard/',views.admindashboard, name="dashboard"),
    path('addadmin/', views.addadmins,name ='addadmin'),
    path('customers/', views.C_details,name='customers'),
    path('customers/',include('customer.urls')),
    path('login/', views.adminlogin,name='login'),
    path('loginredirect/',views.login_redirect),
    path('logout/', views.signout,name='logout'),
    path('products/', views.p_details,name='products'),
    path('update/<int:edit_id>', views.admin_update),
    path('products/', include('product.urls')),

]