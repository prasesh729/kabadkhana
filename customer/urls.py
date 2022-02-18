from django.contrib import admin
from django.urls import path
from customer import views



urlpatterns = [
    path('c_delete/<int:id>' ,views.customer_delete)
]