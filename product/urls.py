from django.contrib import admin
from django.urls import path
from product import views



urlpatterns = [
    path('edit/', views.product_edit,name='edit'),
    path('delete/<int:product_id>' ,views.product_delete,name='delete')


]