from django.db import models
from customer.models import User
# Create your models here.


class Products(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    p_name = models.CharField(max_length=100,blank=True)
    p_category =models.CharField(max_length=100,blank=True)
    p_description =models.TextField(max_length=300,blank=True)
    p_quantity=models.PositiveIntegerField()
    p_price=models.PositiveIntegerField()
    p_image=models.ImageField(upload_to='product_img',blank=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,default=17)

    class Meta:
        db_table = "product_tbl"

class Booking(models.Model):
    pro_id= models.ForeignKey(Products,on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=20)
    full_name =models.CharField(max_length=30)
    phone_no =models.CharField(max_length=11)
    date = models.DateTimeField()
    address= models.DateTimeField()

