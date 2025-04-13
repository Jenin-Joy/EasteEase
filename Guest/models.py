from django.shortcuts import render
from Admin.models import *

# Create your views here.
class tbl_user(models.Model):
    
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to='Assets/user/photo')
    user_password=models.CharField(max_length=50)
    


class tbl_owner(models.Model):
    owner_status=models.IntegerField(default=0)
    owner_name=models.CharField(max_length=50)
    owner_email=models.CharField(max_length=50)
    owner_contact=models.CharField(max_length=50)
    owner_address=models.CharField(max_length=50)
    owner_place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    owner_photo=models.FileField(upload_to='Assets/user/photo')
    owner_password=models.CharField(max_length=50)    